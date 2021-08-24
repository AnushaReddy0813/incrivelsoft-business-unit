from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Business(TimeStampModel):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    emp_size=models.IntegerField(default=0)
    owner_name=models.CharField(max_length=100,default='')
    mobile=models.CharField(max_length=10,default='')
    def __str__(self):
        return self.title

