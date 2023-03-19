from rest_framework.authentication import TokenAuthentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import gettext_lazy as _


class URLTokenAuthentication(TokenAuthentication):

    keyword = 'token'

    '''
    Authenticate the user token from url
    v2ray user subscribe proxies will use this way
    Please be sure to use it in https environment 
    '''

    def authenticate(self, request):
        token = request.query_params.get(self.keyword)
        if token:
            return self.authenticate_credentials(token.strip())
        return False
