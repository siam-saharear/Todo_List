from django.shortcuts import render, redirect, get_object_or_404

from django.utils.timezone import now

import calendar
from calendar import HTMLCalendar

from .forms import *
from .models import *

# Create your views here.
def base_func(request,year=None, month=None, day=None):
    if year==None and month==None and day==None:
        date = now().date()
    else:
        date = f"{year}-{month}-{day}"
    print(date)
        
    individual_tasks = Task.objects.filter(category=None).filter(creation_time__date = date)
    categories = Category.objects.filter(creation_time__date = date)
        
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

    
def previous_next_month(month_index):
    if month_index == 12 or month_index == 1:
        if month_index == 12:
            next_month = 1
            previous_month = 11
            year_change = 1
            
        elif month_index ==1:
            previous_month == 12
            next_month = 2
            year_change = -1
            
    elif month_index != 12 or month_index != 1:
        previous_month = month_index - 1
        next_month = month_index + 1
        year_change = 0
        
    else:
        return ValueError()
    return previous_month, next_month, year_change



def previous_next_year(year, year_change):
    if year_change == 0:
        previous_year = year -1
        next_year = year + 1




def calendar_func(request, year=None, month=None):

    if year==None and month==None:
        year = now().year
        month = now().month
        

    elif year!=None and month!=None:
        if month>12:
            month = 1
            year += 1
        elif month <1:
            month = 12
            year -= 1

    next_month = month + 1
    previous_month = month - 1
    
    next_year = year + 1
    previous_year = year -1
        
    month_calendar = calendar.monthcalendar(year, month)  
    context = {"month":month,
               "next_month":next_month,
               "previous_month":previous_month,
               
               "year":year,
               "next_year":next_year,
               "previous_year":previous_year,
               
               "month_calendar":month_calendar}
    return render(request, "objectives/calendar.html", context)
    # return redirect("base")
    