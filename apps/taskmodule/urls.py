from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('taskform',views.taskform),
    path('itemform',views.itemform),
    path('activityform',views.activityform),
    path('singleitem/<int:iId>',views.singleitem, name='singleitem'),
    path('singleactivity/<int:aId>',views.singleactivity, name= 'singleactivity'),
    path('singletask/<int:tId>',views.singletask, name= 'singletask'),
    path('display_activity',views.display_activity),
    path('display_task',views.display_task),
    path('display_item',views.display_item),
    path('addTask',views.add_task),
    path('addItem',views.add_item),
    path('addActivity',views.add_activity),
    path('search',views.search_filter),
    path('update_item/<int:iId>', views.update_item, name= 'update_item'),
    path('update_item_message', views.update_item_message, name= 'update_item_message'),
] 