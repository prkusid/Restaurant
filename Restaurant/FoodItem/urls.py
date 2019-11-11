
from django.urls import path
from FoodItem import views

urlpatterns = [
    path('', views.home),
    path('details/<int:id>/<item_name>', views.deatils),
    path('employees', views.employees_or_steps),
    path('employee_details/<assigned>', views.employee_details),
    path('step_details/<process_step>', views.step_details),
]
