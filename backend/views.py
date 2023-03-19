from django.http import HttpResponseNotFound, JsonResponse
from backend.models import ProxyNode
from backend.shortcuts import gen_config


# Create your views here.
def get_config(request):
    node_address = request.META.get("REMOTE_ADDR")
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        node_address = request.META.get("HTTP_X_FORWARDED_FOR")
    proxynode, created = ProxyNode.objects.get_or_create(server=node_address)
    if created:
        proxynode.confirmed = True
        proxynode.save()
    v2rayconfig = gen_config(proxynode)
    return JsonResponse(v2rayconfig)