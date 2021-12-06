from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

from .models import Task
from .forms import TaskForm

def index(request):

    num_tasks = Task.objects.filter(completed=0).count()
    completed_tasks = Task.objects.filter(completed=1).count()
    
    task_list = Task.objects.order_by("due_date")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')

    form = TaskForm()


    context = {
        'num_tasks': num_tasks,
        'completed_tasks': completed_tasks,
        'forms': form,
        "list": task_list,
        "title": "TODO LIST",
    }

    return render(request, 'index.html', context=context)

def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Task removed!")
    return redirect('todo')

def complete(request, item_id):
    item = Task.objects.get(id=item_id)
    item.completed = 1
    item.save()
    return redirect('todo')