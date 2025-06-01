from django.shortcuts import render, redirect, get_object_or_404

from django.utils.timezone import now

import calendar
from calendar import HTMLCalendar

from .forms import *
from .models import *

# Create your views here.
def base_func(request):
    today = now().date()
    individual_tasks = Task.objects.filter(category=None).filter(creation_time__date = today)
    categories = Category.objects.filter(creation_time__date = today)

    categorized_tasks = []
    for category in categories:
        tasks = None
        try:
            tasks = Task.objects.filter(category = category)
        except:
            print(f"The Category {category.name} \ndoes not have any task.  ")
        categorized_tasks.append({
            "category": category,
            "tasks" : tasks
            
        })
    return render(request, "objectives/homepage.html", {"individual_tasks":individual_tasks, "categories":categories, "categorized_tasks":categorized_tasks})

def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base")
        else:
            print("form error")
    return render(request, "objectives/category_creation.html", {"form":form})


def create_task(request, category_uuid=None):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            if category_uuid!=None:
                category = Category.objects.get(uuid=category_uuid)
                task.category = category
            task.save()
            return redirect("base")
        else:
            print("Form error")            
    return render(request, "objectives/task_creation.html", {"form":form})

def change_status(request, task_uuid):
    task = Task.objects.get(uuid = task_uuid)
    task.status = not task.status
    task.save()
    print(f"task status changed to \n{task.status}")
    return redirect("base")
    
    
def edit_task(request, task_uuid):
    task = Task.objects.get(uuid = task_uuid)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("base")
    else:
        form = TaskForm(instance=task)
    return render(request, "objectives/edit_task.html", {"form":form})

def delete_task(request, task_uuid):
    task = Task.objects.get(uuid = task_uuid)
    task.delete()
    return redirect("base")


def delete_category(request, category_uuid):
    category = Category.objects.get(uuid = category_uuid)
    category.delete()
    return redirect("base")


def calendar_func(request):
    all_tasks = Task.objects.all().order_by("creation_time")
    first_instance_month = all_tasks.first().creation_time.month
    first_instance_year = all_tasks.first().creation_time.year
    
    month_calendar = calendar.monthcalendar(first_instance_year, first_instance_month)

    return render(request, "objectives/calendar.html", {"month_calendar":month_calendar})
    # return redirect("base")