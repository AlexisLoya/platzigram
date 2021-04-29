from django.db import models

# Create your models here.


class User(models.Model):
    """ user model """

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateTimeField(blank=True, null=True)

    country = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)

    # like toString in java
    def __str__(self):
        return super().__str__()
