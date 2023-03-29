from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    id=models.AutoField(primary_key=True)
    employee_name=models.CharField(default='',max_length=25,verbose_name="Name")
    employee_designation=models.CharField(default='',max_length=30,verbose_name="Designation")
    contact_number=models.IntegerField(default='',verbose_name="Contact Number")

    def __str__(self):
        return self.employee_name