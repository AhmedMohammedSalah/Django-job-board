from django.db import models

# Create your models here.

'''
django model field :
    html widjet 
    validation 
    db size 
'''
JOB_TYPE =(
    ("Part Time","Part Time"),
    ("Full Time","Full Time"),
)
class Job(models.Model):# as atable 
    title =models.CharField(max_length=100) # as Column 
    # location 
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy =models.IntegerField(default=1) 
    salary =models.IntegerField(default=0) 
    # catogry 
    # Relations 
    exprience=models.IntegerField(default=0) 

    def __str__(self):
        return self.title