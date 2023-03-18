from celery import shared_task
from v2client import V2RayClient
from v2client import enum as v2types

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


client = V2RayClient("v2ray", 8080)

# add user to nodes
# TODO will call every proxy node
@shared_task
def v2ray_add_user(email):
    # ADD VMESS USER
    client.add_user(
        inbound_tag="users",
        proxy_type=v2types.ProxyTypes.VMESS,
        email=email,
        level=0,
        security=v2types.VMessSecurityTypes.AUTO,
        user_id=email
    )


# delete user in nodes
# TODO will call every proxy node, let remove this email user
@shared_task
def v2ray_del_user(email):
    # ADD VMESS USER
    client.remove_user(inbound_tag="users", email=email)


# analysis all accounts
@shared_task
def v2ray_users_traffic():
    resp = client.query_stats('user>>>')
    logger.info(str(resp))


# analysis proxy node network traffic
# TODO send node network traffic to main server
@shared_task
def v2ray_system_traffic():
    resp = client.get_sys_stats()
    logger.info(str(resp))
