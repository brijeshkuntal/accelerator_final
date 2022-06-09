from multitenant_app.models import Tenant
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.http import Http404
from tenant_schemas.utils import get_tenant_model, remove_www_and_dev, get_public_schema_name
from django.db import utils


class TenantTutorialMiddleware(object):
    def process_request(self, request):
        connection.set_schema_to_public()
        hostname_without_port = remove_www_and_dev(request.get_host().split(':')[0])

        TenantModel = get_tenant_model()

        try:
            request.tenant = TenantModel.objects.get(domain_url=hostname_without_port)
        except utils.DatabaseError:
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
            return
        except TenantModel.DoesNotExist:
            if hostname_without_port in ("127.0.0.1", "localhost"):
                request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
                return
            else:
                raise Http404

        connection.set_tenant(request.tenant)
        ContentType.objects.clear_cache()

        # if hasattr(settings, 'PUBLIC_SCHEMA_URLCONF') and request.tenant.schema_name == get_public_schema_name():
        #     request.urlconf = settings.PUBLIC_SCHEMA_URLCONF

class VerifyHostMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = self.tenant_from_request(request)
        if not tenant:
            return HttpResponseForbidden("You are not allowed to access the platform.")
        request.tenant = tenant
        # print(request, dir(request))
        return self.get_response(request)

    def hostname_from_request(self, request):
        # split on `:` to remove port
        return request.get_host().split(':')[0].lower()

    def tenant_from_request(self, request):
        hostname = self.hostname_from_request(request)
        subdomain_prefix = hostname.split('.')[0]
        return Tenant.objects.filter(name=subdomain_prefix, is_active=True).first()

