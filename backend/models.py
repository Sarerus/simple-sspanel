from django.db import models
from decimal import Decimal
from django.utils.translation import gettext as _
from core.models import Base
from sspanel.models import Account

# Base class for all nodes
class Node(Base):
    # Domain or ip address
    server = models.CharField(
        _("Server"),
        max_length=128,
        unique=True,
        help_text=_("Domain name or server address"))

    # Whether the node has confirmed
    confirmed = models.BooleanField(
        _("Confirmed"),
        default=False,
        help_text=_("Automatically discover the host, whether it has been confirmed, the confirmed host will receive the user configuration and use it"))

    class Meta:
        verbose_name = _("Node")
        verbose_name_plural = _("Node")
        abstract = True


class ProxyNode(Node):
    PROTOCAL_VMESS = "vmess"
    PROTOCAL_VLESS = "vless"
    PROTOCAL_TROJAN = "trojan"
    PROTOCAL_SSR = "ssr"
    PROTOCAL_SS = "ss"

    NODE_CHOICES = (
        (PROTOCAL_VMESS, PROTOCAL_VMESS),
        (PROTOCAL_VLESS, PROTOCAL_VLESS),
        (PROTOCAL_TROJAN, PROTOCAL_TROJAN),
        (PROTOCAL_SSR, PROTOCAL_SSR),
        (PROTOCAL_SS, PROTOCAL_SS),
    )

    # This node name sort description
    name = models.CharField(
        _("Name"), 
        null=True,
        max_length=128)

    # Proxy support protocal
    protocal = models.CharField(
        _("Protocal"), 
        default=PROTOCAL_VMESS, 
        choices=NODE_CHOICES, 
        max_length=128)

    # V2ray-core request config with this token
    token = models.CharField(
        _("Token"), 
        null=True,
        blank=True,
        max_length=128)

    # node level
    level = models.PositiveIntegerField(
        _("Level"), 
        default=0)

    # mirror node, etc. cdn domains
    mirror = models.BooleanField(
        _("Mirror"), 
        default=False,
        help_text=_('This node is the mirror image of other source nodes, but the domain name is different, please select'))

    # network traffic used
    traffic_used = models.BigIntegerField(
        _("traffic used"), 
        default=0)

    # The total network traffic
    traffic_total = models.BigIntegerField(
        _("traffic total"), 
        default=0)

    # network traffic weight
    traffic_weight = models.DecimalField(
        _("Weight"),
        default=Decimal("1.0"),
        decimal_places=2,
        max_digits=6,
    )

    class Meta:
        verbose_name = _("Proxy Node")
        verbose_name_plural = _("Proxy Node")


class AccountTraffic(Base):

    # foreign sspanel account
    account = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE, 
        verbose_name=_('sspanel account'))

    proxy_node = models.ForeignKey(
        ProxyNode,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Traffic node'))
    
    traffic_up = models.BigIntegerField(
        _('Upload traffic'), 
        default=0)

    traffic_down = models.BigIntegerField(
        _('Download traffic'), 
        default=0)

    class Meta:
        verbose_name = _("User traffic records")
        verbose_name_plural = _("User traffic records")
