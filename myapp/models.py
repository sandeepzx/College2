from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(default=1, max_length=50)

class Usermember(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Age = models.IntegerField(null=True)
    Number = models.CharField( max_length=50)
    Image = models.ImageField( upload_to='Images/',null=True, height_field=None, width_field=None, max_length=None)