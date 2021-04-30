"""User admin classes"""
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Model
from users.models import Profile
from  django.contrib.auth.models import User
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    #View principal table
    list_display = ('pk','user','phone_number','website','picture')

    #add hyperlink
    list_display_links = ('pk','user')

    #add editable fields
    list_editable = ('phone_number','website','picture')

    #add filters
    search_fields = ('user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name',
                     'phone_number')

    list_filter = ('user__is_active','user__is_staff','created','modified')

    #tupla
    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),
                    ('phone_number', 'website'),)
        }),
        ('Extra info',{
            'fields':(
                ('biography',)
            )
        }),
        ('Metadata', {
            'fields': ((('created','modified'),)
            )
        }),
    )
#fields only read
    readonly_fields = ('created','modified',)

#Register User and profile at the same time
class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)