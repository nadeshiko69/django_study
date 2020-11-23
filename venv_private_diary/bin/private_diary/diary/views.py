from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

class IndexView(generic.TemplateView):
    template_name = "index.html"