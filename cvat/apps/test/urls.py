# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path

from .views import TaskAnnotationCountsView

urlpatterns = [
    path(
        "test/tasks/<int:task_id>/annotation_counts/",
        TaskAnnotationCountsView.as_view(),
        name="test-task-annotation-counts",
    ),
]
