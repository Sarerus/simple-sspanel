from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from backend.tasks import v2ray_add_user
from sspanel.authentication import URLTokenAuthentication
from sspanel.shortcuts import generate_subscribe
from sspanel.models import Account

# Create your views here.
class SubscribeView(APIView):

    """
    Return the corresponding configuration file according to the client type
    """

    authentication_classes = [URLTokenAuthentication]
    permission_classes = [IsAuthenticated]

    # v2ray client identify key
    keyword = 'client'

    def get(self, request):
        client = request.query_params.get(self.keyword)
        if client is None:
            # return default configuration file
            client = ''
        # TODO implemance
        if not hasattr(request.user, 'account'):
            # create account for user
            account = Account.objects.create(user=request.user)
            # add new account to v2ray service
            v2ray_add_user.delay(account.uuid)
        raw_text = generate_subscribe(request.user.account, client)
        return HttpResponse(content=raw_text, content_type='text/plain')