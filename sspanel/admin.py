from django.contrib import admin
from django.utils.translation import gettext as _
from sspanel.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'user_username',
        'uuid',
        'level',
        'remark',
        'create_time',
    ]
    fieldsets = [
        (None, {
            'fields': [
                'username',
                'password',
                'uuid',
                'level',
            ]
        }
        ),
        (_('General Information'),
            {
                'fields': [
                    'remark',
                    'status',
                    'enable',
                ]
        }
        ),
    ]

    @admin.display(ordering='user__username', description=_('Username'))
    def user_username(self, obj):
        return obj.user.username

    def get_queryset(self, request):
        return super(AccountAdmin, self).get_queryset(request).select_related('user')
