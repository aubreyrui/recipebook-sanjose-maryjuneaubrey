from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(
        validators = [
            MinLengthValidator(255, "Short bio must be at least 255 characters long!") 
            # ensures that the length of the bio is more than 255 characters
            # https://docs.djangoproject.com/en/5.0/ref/validators/
        ]
    )

# Create your models here.
