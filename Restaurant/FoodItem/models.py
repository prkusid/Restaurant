from django.db import models

# Create your models here.

# Database Table for Food Items Available
class FoodItemsAvailable(models.Model):
    item_name   =   models.CharField(max_length = 50)


# Database Table for Process Step

class ProcessStep(models.Model):
    item_name        =   models.ForeignKey(to=FoodItemsAvailable,on_delete=models.CASCADE)
    sequence_number  =   models.PositiveIntegerField()
    process_step     =   models.CharField(max_length = 50)
    schedule         =   models.CharField(max_length = 10)
    assigned         =   models.CharField(max_length = 30)
