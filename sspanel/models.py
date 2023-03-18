from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from backend.tasks import v2ray_add_user, v2ray_del_user
from core.models import Base

import uuid

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


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

    def save(self, *args, **kwargs):
        if not self.id:
            # create system user
            user = User.objects.create_user(
                username=self.username, 
                password=self.password
            )
            self.user = user 
            # add v2ray user
            v2ray_add_user.delay(self.uuid)
        else:
            # if change account uuid will update v2ray user
            before = Account.objects.get(pk=self.id)
            if self.uuid != before.uuid:
                v2ray_del_user.delay(before.uuid)
                v2ray_add_user.delay(self.uuid)
        return super(Account, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # delete v2ray user
        v2ray_del_user.delay(self.uuid)
        return super(Account, self).delete(*args, **kwargs)
