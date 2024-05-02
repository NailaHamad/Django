from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('taskform',views.taskform),
    path('itemform',views.itemform),
    path('activityform',views.activityform),
    path('singleitem/<int:tId>',views.singleitem),
    path('singleactivity/<int:tId>',views.singleactivity),
    path('singletask/<int:tId>',views.singletask),
    path('display_activity',views.display_activity),
    path('addTask',views.add_task),
    path('addItem',views.add_item),
    path('addActivity',views.add_activity),
    path('search',views.search_filter),
     path('update_item/<int:tId>', views.update_item),
    
] 