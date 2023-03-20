from django.contrib import admin
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.html import format_html
from rest_framework.authtoken.models import Token
from sspanel.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'user_username',
        'uuid',
        'level',
        'subscribe_url',
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

    def get_queryset(self, request):
        self.request = request      
        return super().get_queryset(request)

    @admin.display(description=_('Subscribe Url'))
    def subscribe_url(self, obj):
        token, _ = Token.objects.get_or_create(user=obj.user)
        return format_html(
            u'<a href="{}">{}</a>', 
            f"{ reverse('subscribe_url') }?token={ token.key }", 'clash')

    @admin.display(ordering='user__username', description=_('Username'))
    def user_username(self, obj):
        return obj.user.username

    def get_queryset(self, request):
        return super(AccountAdmin, self).get_queryset(request).select_related('user')
