from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

'''
django model field :
    html widjet 
    validation 
    db size 
'''


def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "jobs/%s/%s.%s" % (instance.id, instance.id, extension)


class Job(models.Model):  # as atable
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # as Column
    # location
    #### use Choices in CharField########
    JOB_TYPE = (
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time"),)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    ###################################
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #### use Choices [1 to many] Relation########
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    # category =models.models.ManyToManyField("app.Model", verbose_name=_(""))('Category',on_delete=models.CASCADE)
    ###############################
    exprience = models.IntegerField(default=0)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(
        Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
