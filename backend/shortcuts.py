
from backend.models import ProxyNode
import json


# Generate v2ray-core configuration file
def gen_config(model: ProxyNode):
    data = {}
    with open('backend/assets/json/v2ray-config.json') as f:
        data = json.load(f)
    if model.enable and model.confirmed:
        # add user to config file
        pass
    return data
