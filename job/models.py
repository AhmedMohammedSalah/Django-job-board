from django.db import models

# Create your models here.

'''
django model field :
    html widjet 
    validation 
    db size 
'''

class Job(models.Model):# as atable 
    title =models.CharField(max_length=100) # as Column 
    # location 
    ####use Choices in CharField########
    JOB_TYPE =(
    ("Part Time","Part Time"),
    ("Full Time","Full Time"),)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    ###################################
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy =models.IntegerField(default=1) 
    salary =models.IntegerField(default=0) 
    ####use Choices [1 to many] Relation########
    category =models.ForeignKey('Category',on_delete=models.CASCADE)

    # category =models.models.ManyToManyField("app.Model", verbose_name=_(""))('Category',on_delete=models.CASCADE)
    ###############################
    exprience=models.IntegerField(default=0) 

    def __str__(self):
        return self.title


class Category(models.Model):
    name =models.CharField(max_length=25)
    def __str__(self):
        return self.name