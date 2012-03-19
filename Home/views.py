# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from models import Home
import Recent_Updates
import settings

#def get_content(content=False):
#	print " @@@@@ settings.ROOT_PATH @@@@@ ",settings.ROOT_PATH
#	return HttpResponse(content,mimetype="text/html")
#	image_data = open("/path/to/my/image.png", "rb").read()
#	return HttpResponse(image_data, mimetype="image/png")


def index(request):
	home = False
        if Home.objects.all():
#            print "::: Home.objects.all = True"
		home = Home.objects.all()[0]
        print ":::::home::",home
	recent_updates = Recent_Updates.models.Recent_Updates.objects.filter(show_on_home = True).order_by("-published_date")
	return render_to_response('index.html',{'home':home, 'recent_updates':recent_updates, 'user':request.user, 'next':request.META['PATH_INFO']})
