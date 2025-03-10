from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TasksForm()
    return render(request, 'task_form.html', {'form': form})

def task_update(request, id):
    task = Tasks.objects.filter(id=id).first()
    if not task:
        return redirect('task_list')

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TasksForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, id):
    task = Tasks.objects.filter(id=id).first()
    if task and request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
