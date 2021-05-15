from django.db import models

class Registr(models.Model):
    username = models.CharField('Username', max_length=50)
    email = models.EmailField('Email', max_length=50)
    password1 = models.CharField('Password', max_length=50)
    password2 = models.CharField('Confirm your password', max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

