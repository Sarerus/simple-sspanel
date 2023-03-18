from django.http import HttpResponseNotFound, JsonResponse
from backend.models import ProxyNode
from backend.shortcuts import gen_config


# Create your views here.
def get_config(request):
    token = request.GET.get('token')
    if token is None:
        return HttpResponseNotFound('')
    proxynode, created = ProxyNode.objects.get_or_create(token=token)
    if created:
        proxynode.server = request.META.get("REMOTE_ADDR")
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            proxynode.server = request.META.get("HTTP_X_FORWARDED_FOR")
        proxynode.save()
    v2rayconfig = gen_config(proxynode)
    return JsonResponse(v2rayconfig)