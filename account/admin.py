from django.contrib.auth import admin
from django.contrib.auth.models import Group
from django.contrib import admin as admn
from .forms import UserCreationForm, UserUpdateForm
from .models import User, OtpCode


@admn.register(OtpCode)
class OtpCodeAdmin(admn.ModelAdmin):
    list_display = ('phone_number', 'code')


class UserAdmin(admin.UserAdmin):

    form = UserUpdateForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_staff')

    list_filter = ('is_active',)
    search_fields = ('email', 'username', 'phone_number')


    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'last_login')})
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'phone_number')}),
    )

    ordering = ('email',)
    filter_horizontal = ()


admn.site.unregister(Group)
admn.site.register(User, UserAdmin)

