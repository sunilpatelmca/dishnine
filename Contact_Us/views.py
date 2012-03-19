# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from models import *
import settings

def contact_us(request):
	contact_us = False
	if Contact_Us.objects.all():
		contact_us=Contact_Us.objects.all()[0]
	return render_to_response('contact_us.html',{'contact_us':contact_us,'user':request.user, 'next':request.META['PATH_INFO']})
