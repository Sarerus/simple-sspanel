from backend.models import ProxyNode
from sspanel.models import Account
from sspanel.types import ClientCategory

import yaml
import base64


# Generate v2ray-core client config file

def _generate_clash_config(account: Account):
    base_config = {}
    with open('sspanel/assets/v2ray/clash.yaml', 'r') as f:
        base_config = yaml.safe_load(f)
    proxies = [
        {
            'name': node.name if node.name else node.server,
            'type': node.protocal,
            'server': node.server,
            'port': 443,
            'tls': True,
            'uuid': str(account.uuid),
            'alterId': 0,
            'cipher': 'auto',
            'network': 'ws',
            'ws-path': '/websocket',
            'ws-headers': { 
                'Host': node.server
            },
            'ws-opts': {
                'path': '/websocket', 
                'headers': { 
                    'Host': node.server
                }
            }
        } for node in ProxyNode.objects.filter(confirmed=True, enable=True)
    ]
    base_config['proxies'] = proxies
    base_config['proxy-groups'][0]['proxies'] = [ p['name'] for p in proxies ]
    base_config['proxy-groups'][1]['proxies'] = [ p['name'] for p in proxies ]
    return yaml.dump(base_config, sort_keys=False)


'''
Generate client subscription file
Support clash
'''

def generate_subscribe(account: Account, client):
    # default clash category(shadowrocket support)
    return _generate_clash_config(account)
