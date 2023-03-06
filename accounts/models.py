from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name="user_city",
                             on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='profile', height_field=None,
                              width_field=None, max_length=None, blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)
