from django.shortcuts import render, redirect


def index(request):
    # study the request
    return render(request, 'taskmodule/index.html') # rendering the template

def task(request):
    # study the request
    return render(request, 'taskmodule/task.html') # rendering the template

def tasks(request, tid):
    # study the request
    task1 = {'id':123, 'priority':'high', 'sec': 'study'}
    task2 = {'id':456, 'priority':'low', 'sec': 'shop'}
    
    targetT =None
    
    if task1['id'] == tid : targetT=task1
    if task2['id'] == tid : targetT=task2
    
    context= {'task':targetT}
    
    if targetT == None : return redirect('/')
    
    return render(request, 'taskmodule/tasks.html', context) # rendering the template


def addTask(request):
    
    return render(request, 'taskmodule/tasks.html') # rendering the template


def today(request):
    
    return render(request, 'taskmodule/today.html') # rendering the template

def projects(request):
    
    return render(request, 'taskmodule/projects.html') # rendering the template

def teams(request):
    
    return render(request, 'taskmodule/team.html') # rendering the template

def task_form(request):
    if request.method = "POST":
        value = request.POST.get('task_name')