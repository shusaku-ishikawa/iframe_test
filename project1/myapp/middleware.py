from django.utils.deprecation import MiddlewareMixin
class DisableCSRF(MiddlewareMixin):
  def process_request(self, request):
    setattr(request, '_dont_enforce_csrf_checks', True)

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # if request.path != '/admin/login/' and not request.user.is_authenticated:
        #     return HttpResponseRedirect('/admin/login/')
        return response
