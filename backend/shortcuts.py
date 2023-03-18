
from backend.models import ProxyNode
import json

from sspanel.models import Account


# Generate v2ray-core configuration file
def gen_config(model: ProxyNode):
    data = {}
    with open('backend/assets/json/v2ray-config.json') as f:
        data = json.load(f)
    if model.enable and model.confirmed:
        for account in Account.objects.filter(enable=True):
            data['inbounds'][1]['settings']['clients'].append(
                {
                    "email": account.uuid, # UUID
                    "id": account.uuid, # UUID
                    "level": account.level,
                    "alterId": 0
                }
            )
    return data
