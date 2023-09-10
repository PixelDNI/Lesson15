from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import *

# Create your views here.


def start_page(request):
    uncompleted_tasks = Task.objects.filter(status=False).order_by('deadline')
    completed_tasks = Task.objects.filter(status=True).order_by('deadline')
    return render(request, 'index.html', {'u_tasks': uncompleted_tasks, 'c_tasks': completed_tasks})


def create_new_task(request):
    if request.method == 'POST':
        form = CreateNewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_page')
        else:
            return render(request, 'create_task.html', {'form': form})
    form = CreateNewTaskForm()
    return render(request, 'create_task.html', {'form': form})


def update_task(request, id):
    obj = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('start_page')
    else:
        form = UpdateTaskForm(instance=obj)

    return render(request, 'update_page.html', {'form': form})


def delete_task(request, id):
    obj = get_object_or_404(Task, id=id)
    if obj:

        obj.delete()
        return redirect('start_page')

    return render(request, 'delete_task.html')


def change_status(request, id):
    obj = get_object_or_404(Task, id=id)
    if obj.status == True:
        obj.status = False
        obj.save()
    else:
        obj.status = True
        obj.save()

    return redirect('start_page')