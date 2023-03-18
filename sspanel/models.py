from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from core.models import Base

# Create your models here.
class Account(Base):

    # foreign system user
    account = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_('System Account'))
    
    # uuid for v2ray client
    uuid = models.UUIDField(
        'UUID',
        unique=True,
        help_text=_('V2ray-core client uuid'))

    # user level for v2ray-core client field
    level = models.PositiveIntegerField(
        _('User Level'), 
        default=0)