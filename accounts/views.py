# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
import settings
from models import Terms_Service
from django.contrib.auth import logout, login

def get_terms(request, group=None, terms_template_name = 'register_terms.html'):
	term = False
	if Terms_Service.objects.all():
		term = Terms_Service.objects.all()[0]
	if request.META.has_key('HTTP_REFERER'):
		next = request.META['HTTP_REFERER']
	else:
		next = '.'
	return render_to_response(terms_template_name, {'term':term, 'user':request.user, 'next':next}, context_instance = RequestContext(request))

def account_logout(request):
	logout(request)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

#def account_login(request):
#	login(request)
#	if request.GET.has_key('next'):
#		if request.GET['next']:
#			next = request.GET['next']
#		else:
#			next = '/'
#	elif request.POST.has_key('next'):
#		if request.POST['next']:
#			next = request.POST['next']
#		else:
#			next = '/'
#	else:
#		next = '/'
#			
#       return HttpResponseRedirect(next)
