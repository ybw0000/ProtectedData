from django.db import models

class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    phone = models.CharField('Phone number', max_length=20)
    message = models.TextField('Text message')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
