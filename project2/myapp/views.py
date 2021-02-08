from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def myview(request):
  template_name = 'iframe.html'
  return render(request, template_name)