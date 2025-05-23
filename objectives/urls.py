from django.urls import path
from . import views

urlpatterns = [
    path("", views.base_func, name="base"),
    path("category_creation/", views.create_category, name="category_creation"),
    path("task_creation/<uuid:category_uuid>", views.create_task, name="task_creation"),
    path("task_creation/", views.create_task, name="task_creation"),
    path("change_status/<uuid:task_uuid>", views.change_status, name="change_status"),
    
    
]
