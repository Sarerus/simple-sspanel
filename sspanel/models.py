from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from core.models import Base

import uuid


# Create your models here.
class Account(Base):

    # foreign system user
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_('System Account'))

    # TODO temp alias to user.username
    username = models.CharField(
        _('temp username'), 
        null=True,
        max_length=128)

    # TODO temp alias to user.password
    password = models.CharField(
        _('temp password'), 
        null=True,
        max_length=128)
    
    # uuid for v2ray client
    uuid = models.UUIDField(
        'UUID',
        unique=True,
        default=uuid.uuid4,
        help_text=_('V2ray-core client uuid'))

    # user level for v2ray-core client field
    level = models.PositiveIntegerField(
        _('User Level'), 
        default=0)