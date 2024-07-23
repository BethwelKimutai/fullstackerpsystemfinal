from django.contrib import admin
from django.core.mail import send_mail
from .models import Company, User, UserOTP


# Define custom admin classes
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


class UserOTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')




admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserOTP, UserOTPAdmin)
