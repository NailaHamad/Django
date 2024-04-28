from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('taskform',views.taskform),
    path('tasks/<int:bId>',views.task),
    path('display-activity',views.display_activity),
    path('add-task',views.add_task),
    path('add-item',views.add_item),
    path('edit-item',views.edit_item),
    path('today',views.today),
    path('projects',views.projects),
    path('team',views.teams),
    path('search',views.search_filter),
    
    
] 