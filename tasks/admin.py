from django.contrib import admin
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.admin import SocialAppAdmin
from .models import Task

# Unregister the default admin
admin.site.unregister(SocialApp)
admin.site.register(Task)

# Re-register with your customizations
@admin.register(SocialApp)
class CustomSocialAppAdmin(SocialAppAdmin):
    list_display = ('provider', 'name', 'client_id')
