from django.shortcuts import render
from FoodItem.models import FoodItemsAvailable,ProcessStep
from django.db.models import Q

# Create your views here.

def home(request):
    food_items  =   FoodItemsAvailable.objects.all()
    return render(request,'FoodItem/home.html',{'food_items':food_items})

def deatils(request,id,item_name):
    process_step =  ProcessStep.objects.filter(item_name = id)
    return render(request,'FoodItem/process_details.html',{'process_step':process_step,'item_name':item_name})

def employees_or_steps(request):
    if request.method == 'POST':
        search  =   True
        search  =   request.POST['search']
        employees   =   ProcessStep.objects.filter(assigned__icontains = search)
        steps       =   ProcessStep.objects.filter(process_step__icontains = search)

        set_employees  =   set()
        for employee in employees:
            set_employees.add(employee.assigned)
        list_employees  =   list(set_employees)

        set_steps  =   set()
        for step in steps:
            set_steps.add(step.process_step)
        list_steps  =   list(set_steps)

        return render(request,'FoodItem/employees_or_steps.html',{'list_employees':list_employees,'list_steps':list_steps,'search':search})

    else:
        search  = False
        employees    =   ProcessStep.objects.values_list('assigned')
        steps    =   ProcessStep.objects.values_list('process_step')

        set_employees  =   set()
        for employee in employees:
            set_employees.add(employee[0])
        list_employees  =   list(set_employees)
        list_employees.remove("")
        list_employees.sort()

        set_steps  =   set()
        for step in steps:
            set_steps.add(step[0])
        list_steps  =   list(set_steps)
        list_steps.sort()

        return render(request,'FoodItem/employees_or_steps.html',{'list_employees':list_employees,'list_steps':list_steps,'search':search})

def employee_details(request,assigned):
    employee_details =  ProcessStep.objects.filter(assigned = assigned)
    return render(request,'FoodItem/employee_details.html',{'employee_details':employee_details,'assigned':assigned})

def step_details(request,process_step):
    step_details =  ProcessStep.objects.filter(process_step = process_step)
    return render(request,'FoodItem/steps_details.html',{'step_details':step_details,'step':process_step})
