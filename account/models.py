from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile',on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    check = models.BooleanField(default=False)
    def __str__(self):
        return f'Profile for user {self.user.username}'


class wholesale_pass (models.Model):
    wpass = models.CharField(max_length=50)
