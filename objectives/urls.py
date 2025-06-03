from django.urls import path
from . import views

urlpatterns = [
    path("", views.base_func, name="base"),
    
    path("task_creation/<uuid:category_uuid>", views.create_task, name="task_creation"),
    path("task_creation/", views.create_task, name="task_creation"),
    path("change_status/<uuid:task_uuid>/", views.change_status, name="change_status"),
    path("edit_task/<uuid:task_uuid>/", views.edit_task, name="edit_task"),
    path("delete_task/<uuid:task_uuid>/", views.delete_task, name= "delete_task"),
    
    path("category_creation/", views.create_category, name="category_creation"),
    path("delete_category/<uuid:category_uuid>/", views.delete_category, name= "delete_category"),
    
    path("calendar/", views.calendar_func, name="calendar"),
    path("calendar/<int:year>/<int:month>", views.calendar_func, name="calendar"),
]
