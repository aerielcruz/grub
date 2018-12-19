from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Restaurant


@receiver(post_save, sender=User)
def create_restaurant(sender, instance, created, **kwargs):
    if created:
        Restaurant.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_restaurant(sender, instance, **kwargs):
    instance.restaurant.save()