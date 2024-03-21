from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('task',views.task),
    path('add-task',views.addTask),
    path('today',views.today),
    path('projects',views.projects),
    path('team',views.teams),
    
    
] 