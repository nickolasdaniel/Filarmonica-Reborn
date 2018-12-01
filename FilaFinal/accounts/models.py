from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagine = models.ImageField(upload_to="profile_pictures", blank=True)
    numar_telefon = models.IntegerField(default = 0)
    cont_instagram = models.URLField(default = '')
    cont_facebook = models.URLField(default = '')
    descriere = models.CharField(max_length = 200, default = '')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender=User)

# Create your models here.
