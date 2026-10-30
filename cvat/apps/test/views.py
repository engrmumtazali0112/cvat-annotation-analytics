# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from collections import Counter

from django.db.models import Count
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cvat.apps.engine.models import LabeledImage, LabeledShape, LabeledTrack, Task
from cvat.apps.engine.permissions import TaskPermission


def count_annotations_by_label(task: Task) -> dict[str, int]:
    """Count top-level annotations (images, shapes, tracks) per label name for a task.

    Skeleton elements (rows with a parent) are skipped so that a skeleton counts once.
    A track counts once, not once per frame.
    """
    counts: Counter[str] = Counter()

    for model in (LabeledImage, LabeledShape, LabeledTrack):
        queryset = model.objects.filter(job__segment__task_id=task.id)
        if hasattr(model, "parent"):
            queryset = queryset.filter(parent__isnull=True)

        rows = queryset.values("label__name").annotate(count=Count("id")).order_by()
        for row in rows:
            counts[row["label__name"]] += row["count"]

    return dict(counts)


class TaskAnnotationCountsView(APIView):
    # Replaces the default PolicyEnforcer, which requires a ViewSet; the task-level
    # check is done explicitly in get() with the same OPA policy the engine uses.
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["test"],
        summary="Get annotation counts per label for a task",
    )
    def get(self, request, task_id: int):
        task = get_object_or_404(
            Task.objects.select_related("organization", "project"), pk=task_id
        )

        permission = TaskPermission.create_base_perm(
            request, self, TaskPermission.Scopes.VIEW_ANNOTATIONS, None, obj=task
        )
        if not permission.check_access().allow:
            raise PermissionDenied()

        counts = count_annotations_by_label(task)
        labels = task.get_labels().values_list("name", flat=True)

        return Response(
            {
                "task_id": task.id,
                "total": sum(counts.values()),
                "counts": [
                    {"label": name, "count": counts.get(name, 0)}
                    for name in sorted(set(labels) | set(counts))
                ],
            }
        )
