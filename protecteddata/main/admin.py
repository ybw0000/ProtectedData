from django.contrib import admin

from .models import Contact, Invite, Newsletter

admin.site.register(Contact)
admin.site.register(Invite)
admin.site.register(Newsletter)
