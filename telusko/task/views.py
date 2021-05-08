from django.shortcuts import render, redirect
from .models import Task

# Create your views here.



def index(request):
    return render(request,'index.html')

def home(request, username):
    task = Task.objects.filter(username=username)
    return render(request,'home.html',{'name':username,'task':task})


def add_task(request):
     task_name=request.POST['task_name']
     task_description=request.POST['task_description']
     username = request.POST['username']
     task = Task(task_name=task_name,task_description=task_description,username=username)
     task.save()
     url = "/home/{}".format(username)
     return redirect(url)
def delete(request):
    id = request.POST['id']
    username = request.POST['username']
    a = Task.objects.get(id=id)
    a.delete()
    url = "/home/{}".format(username)
    return redirect(url)
