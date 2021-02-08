

from django.views.generic import (
  TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def ajax(request):
  print(request.user)
  return JsonResponse({
    'test': 'test'
  })
class MyView(LoginRequiredMixin, TemplateView):
  login_url = '/admin/'
  template_name = 'login.html'
  def post(self, request):
    return HttpResponse('HELLO')