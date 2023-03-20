from django.db import models
from django.utils.translation import gettext as _


# Global base abstract model
class Base(models.Model):
    # object notes
    remark = models.CharField(_('Remark'), max_length=128, null=True, blank=True)

    # object status
    status = models.IntegerField(_('Status'), default=0)

    # Is this object enabled or disable
    enable = models.BooleanField(_('Enable'), default=True)

    # object last update time
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)
    
    # object create time
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)

    class Meta:
        abstract = True
