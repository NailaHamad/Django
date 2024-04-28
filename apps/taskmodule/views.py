from django.shortcuts import render, redirect
from .models import activity, items, task
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg

def index(request):
    # study the request
    return render(request, 'taskmodule/index.html') # rendering the template


def taskform(request):
    # study the request
    return render(request, 'taskmodule/taskform.html') # rendering the template

def activityform(request):
    # study the request
    return render(request, 'taskmodule/activityform.html') # rendering the template
def itemform(request):
    # study the request
    return render(request, 'taskmodule/itemform.html') # rendering the template



def singleitem(request, tId):
    obj = items.objects.get(id = tId)
    return render(request, 'taskmodule/singlitem.html', {'item':obj}) # rendering the template

def singletask(request, tId):
    obj = task.objects.get(id = tId)
    return render(request, 'taskmodule/singletask.html', {'task':obj}) # rendering the template

def singleactivity(request, tId):
    obj = activity.objects.get(id = tId)
    return render(request, 'taskmodule/singleactivity.html', {'activity':obj}) # rendering the template



def add_task(request):
    if request.method == 'POST':
        nameval = request.POST.get('task_name')
        priorityval = request.POST.get('task_priority')
        categoryval = request.POST.get('task_category')
 
        obj = task.objects.create(name= nameval, priority = priorityval,category = categoryval)
        obj.save()
        return redirect('singletask', tId = obj.id)
    return render(request, "taskmodule/taskform.html", {})

def add_activity(request):
    if request.method == 'POST':
        nameval = request.POST.get('activity_name')
        categoryval = request.POST.get('activity_category')
        obj = activity.objects.create(name= nameval,category = categoryval)
        obj.save()
        return redirect('singleactivity', aId = obj.id)
    return render(request, "taskmodule/taskform.html", {})
    
def add_item(request):
    if request.method == 'POST':
        nameval = request.POST.get('items_name')
        categoryval = request.POST.get('items_category')
        priceval = request.POST.get('items_price')
 
        obj = task.objects.create(name= nameval,category = categoryval, price = priceval)
        obj.save()
        return redirect('singleitem', tId = obj.id)
    return render(request, "taskmodule/itemform.html", {})


def display_activity(request):
    obj= activity.objects.all()
    context= {'activity': obj}
    return render(request,'taskmodule/display_activity.html' , context )

def display_item(request):
    pass



def update_item(request):
    pass


def list_activity(request):
    pass

def list_item(request):
    pass
""""
def addTask(request):
    
    return render(request, 'taskmodule/tasks.html') # rendering the template

"""
def today(request):
    
    return render(request, 'taskmodule/today.html') # rendering the template

def projects(request):
    
    return render(request, 'taskmodule/projects.html') # rendering the template

def teams(request):
    
    return render(request, 'taskmodule/team.html') # rendering the template

def __getTask():
    free_time_activities_list = []
    act1 = {'name':'Running in the park', 'category': 'Sports and Fitness'}
    free_time_activities_list.append(act1)
    act2 = {'name':'Yoga or meditation session', 'category': 'Sports and Fitness'}
    act3 = {'name':'Playing basketball or soccer', 'category': 'Sports and Fitness'}
    act4 = {'name':'Cycling or hiking trails', 'category': 'Sports and Fitness'} 
    
    act5 = {'name':'Painting or drawing', 'category': 'Hobbies and Crafts'}
    act6 = {'name':'Knitting or crocheting', 'category': 'Hobbies and Crafts'}
    act7 = {'name':'Woodworking or DIY projects', 'category': 'Hobbies and Crafts'}
    act8 = {'name':'Gardening or planting', 'category': 'Hobbies and Crafts'}
    
    
    act9 = {'name':'Watching a movie or TV series', 'category': 'Entertainmen'}  
    act10 = {'name':'Playing video games', 'category': 'Entertainmen'}
    act11 = {'name':'Listening to music or podcasts', 'category': 'Entertainmen'}
    act12 = {'name':'Reading a book or magazine', 'category': 'Entertainmen'} 
    
    
    act13 = {'name':'Online courses or tutorials', 'category': 'Learning and Skill Development'} 
    act14 = {'name':'Learning a new language', 'category': 'Learning and Skill Development'} 
    act15 = {'name':'Coding or programming projects', 'category': 'Learning and Skill Development'} 
    act16 = {'name':'Cooking or baking new recipes', 'category': 'Learning and Skill Development'} 
    
    
    act17 = {'name': 'Organizing a virtual hangout with friends', 'category': 'Social Activities'}
    act18 = {'name': 'Attending a local community event', 'category': 'Social Activities'}
    act19 = {'name': 'Volunteering for a cause', 'category': 'Social Activities'}
    act20 = {'name': 'Hosting a game night or potluck', 'category': 'Social Activities'}
    
    
    act21 = {'name': 'Taking a bubble bath', 'category': 'Relaxation and Self-care'}
    act22 = {'name': 'Practicing mindfulness or meditation', 'category': 'Relaxation and Self-care'}
    act23 = {'name': 'Pampering with skincare or spa treatments', 'category': 'Relaxation and Self-care'}
    act24 = {'name': 'Journaling or writing reflections', 'category': 'Relaxation and Self-care'}
    free_time_activities_list.append(act2)
    free_time_activities_list.append(act3)
    free_time_activities_list.append(act4)
    free_time_activities_list.append(act5)
    free_time_activities_list.append(act6)
    free_time_activities_list.append(act7)
    free_time_activities_list.append(act8)
    free_time_activities_list.append(act9)
    free_time_activities_list.append(act10)
    free_time_activities_list.append(act11)
    free_time_activities_list.append(act12)
    free_time_activities_list.append(act13)
    free_time_activities_list.append(act14)
    free_time_activities_list.append(act15)
    free_time_activities_list.append(act16)
    free_time_activities_list.append(act17)
    free_time_activities_list.append(act18)
    free_time_activities_list.append(act19)
    free_time_activities_list.append(act20)
    free_time_activities_list.append(act21)
    free_time_activities_list.append(act22)
    free_time_activities_list.append(act23)
    free_time_activities_list.append(act24)
    
    return free_time_activities_list 


def search_filter(request):
    if request.method == "POST":
        string = request.POST.get('keyword')
        isName = request.POST.get('option1')
        isCategory = request.POST.get('option2')
        
        
        # now filter
        myTask = activity.objects.filter(category__icontains='sport')
        
        TaskObjs = activity.objects.filter(Q(category__icontains = 'Learning and Skill Development')&
        (Q(name__contains = 'a') | Q(name__contains = 'or')) )
        
        objs = items.objects.aggregate(count_gt=Count('price', filter=Q(price__gt=0)))
        
        number_of_items= items.objects.aggregate(count= Count('id'))
        
        total = activity.objects.filter(name__contains = 'a').count()
        total_ent = activity.objects.filter(category__contains = 'Entertainmen').count()
        
        
        tasks =  __getTask()
        newTasks = []
        for item in tasks:
            contained = False
            if isName and string in item['name'].lower(): contained = True
            if not contained and isCategory and string in item['category'].lower():contained = True
            if contained: newTasks.append(item)
        return render(request, 'taskmodule/tasks.html',{'tasks': newTasks})
    return render(request, 'taskmodule/search_filter.html', {}) 

#def task_form(request):
#    if request.method = "POST":
#        value = request.POST.get('task_name')