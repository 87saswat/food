from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile(instace, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instace)
    else:
        try:
            profile = UserProfile.objects.get(user=instace)
            profile.save()
        except:
            UserProfile.objects.create(user=instace)    