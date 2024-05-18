from django.shortcuts import render, redirect
from .models import activity, items, task
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg
from .forms import ItemsForm, ActivityForm, TaskForm
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



def singleitem(request, iId):
    obj = items.objects.get(id = iId)
    return render(request, 'taskmodule/singleitem.html', {'item':obj}) # rendering the template

def singletask(request, tId):
    obj = task.objects.get(id = tId)
    return render(request, 'taskmodule/singletask.html', {'task':obj}) # rendering the template

def singleactivity(request, aId):
    obj = activity.objects.get(id = aId)
    return render(request, 'taskmodule/singleactivity.html', {'activity':obj}) # rendering the template



def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            return redirect('singletask', tId = obj.id )
    form = TaskForm(None)
    return render(request, "taskmodule/addtask.html", {'form':form})


def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            return redirect('singleactivity', aId = obj.id )
    form = ActivityForm(None)
    return render(request, "taskmodule/addactivity.html", {'form':form})

def add_item(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            return redirect('singleitem', iId = obj.id )
    form = ItemsForm(None)
    return render(request, "taskmodule/addItem.html", {'form':form})


def display_activity(request):
    obj= activity.objects.all()
    context= {'activity': obj}
    return render(request,'taskmodule/display_activity.html' , context )

def display_item(request):
    obj= items.objects.all()
    context= {'items': obj}
    return render(request,'taskmodule/display_item.html' , context )

def display_task(request):
    obj= task.objects.all()
    context= {'task': obj}
    return render(request,'taskmodule/display_task.html' , context )


def update_item(request, iId):
    obj = items.objects.get(id = iId)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance= obj)
        if form.is_valid():
            obj.save()
            return redirect('singleitem', iId = obj.id )
        
    form = ItemsForm(instance=obj)
    return render(request, "taskmodule/updateitem.html", {'form':form})


def update_item_message(request):
    return render(request,'taskmodule/item_message.html' )

def search_filter(request):
    if request.method == "POST":
        string = request.POST.get('keyword')
        isName = request.POST.get('option1')
        isCategory = request.POST.get('option2')

        
        queryset = activity.objects.all()

       
        if isName and string:
            queryset = queryset.filter(name__icontains=string)
        if isCategory and string:
            queryset = queryset.filter(category__icontains=string)

        activityi = queryset.values()  
        return render(request, 'taskmodule/display_activity.html', {'activity': activityi})
    
    return render(request, 'taskmodule/search_filter.html', {})


