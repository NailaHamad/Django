from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('task',views.task),
    path('tasks/<int:tid>', views.tasks)
    
] 