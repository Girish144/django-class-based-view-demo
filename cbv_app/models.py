from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    loc=models.CharField(max_length=50)
    department_choice=[
        ('mba','mba'),
        ('mca','mca'),
        ('btech','btech'),
    ]
    department=models.CharField(max_length=50,choices=department_choice)

    def __str__(self):
        return self.name
