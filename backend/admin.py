from django.contrib import admin
from django.utils.translation import gettext as _
from backend.models import ProxyNode

# Register your models here.


@admin.register(ProxyNode)
class ProxyNodeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'server',
        'protocal',
        'token',
        'level',
        'confirmed',
        'traffic_used',
        'traffic_total',
        'traffic_weight',
        'create_time',
    ]
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'server',
                'protocal',
                'token',
                'level',
                'confirmed'
            ]
        }
        ),
        (_('General Information'),
            {
                'fields': [
                    'remark',
                    'status',
                    'enable'
                ]
        }
        ),
    ]
