from django.contrib import admin
from FoodItem.models import FoodItemsAvailable,ProcessStep

# Register your models here.

# Admin interface for FoodItemsAvailable Table in Database

class FoodItemsAvailableAdmin(admin.ModelAdmin):
    list_display    =   ['id','item_name']

class ProcessStepAdmin(admin.ModelAdmin):
    list_display    =   ['item_name','sequence_number','process_step','schedule','assigned']


admin.site.register(FoodItemsAvailable,FoodItemsAvailableAdmin)
admin.site.register(ProcessStep,ProcessStepAdmin)
