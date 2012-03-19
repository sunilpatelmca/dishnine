# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from models import *
import settings
from django.contrib.auth.decorators import login_required


def recent_updates(request):
	subjects=[]
	for subject in Subject.objects.all():
		levels=[]
		for level in Level.objects.filter(subject=subject.id):
			recent_updates=[]
			for recent_update in Recent_Updates.objects.filter(subject=subject.id,level=level.id).order_by("-published_date"):
				recent_updates.append({'info':recent_update})
			if recent_updates:
        			levels.append({'id':level.id,'name':level.name,'recent_updates':recent_updates})
        	if levels:
        		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('recent_updates.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
recent_updates = login_required(recent_updates)

def get_recent_update(request, object_id):
	if object_id:
	        get_object_or_404(Recent_Updates, pk = object_id)
		recent_update_object = Recent_Updates.objects.filter(id=object_id)
	subjects=[]
	for recent_update in recent_update_object:
		levels=[]
		recent_updates=[]		
		recent_updates.append({'info':recent_update})
		level = recent_update.level
		levels.append({'id':level.id,'name':level.name,'recent_updates':recent_updates})
		subject = recent_update.subject
		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('recent_updates.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
get_recent_update = login_required(get_recent_update)

def subject_wise_recent_updates(request,subject_id):
	if subject_id:
	        get_object_or_404(Subject, pk = subject_id)
		subject_objects=Subject.objects.filter(id=subject_id)	
	else:
		subject_objects=Subject.objects.all()	
	subjects=[]
	for subject in subject_objects:
		levels=[]
		for level in Level.objects.filter(subject=subject.id):
			recent_updates=[]
			for recent_update in Recent_Updates.objects.filter(subject=subject.id,level=level.id).order_by("-published_date"):
				recent_updates.append({'info':recent_update})
			if recent_updates:
        			levels.append({'id':level.id,'name':level.name,'recent_updates':recent_updates})
        	if levels:
        		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('recent_updates_subject.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
subject_wise_recent_updates = login_required(subject_wise_recent_updates)

def level_wise_recent_updates(request,level_id):
        get_object_or_404(Level, pk = level_id)
        levels=[]
        for level in Level.objects.filter(id=level_id):
		subjects=[]
		for subject in Subject.objects.filter(level=level.id):
			recent_updates=[]
			for recent_update in Recent_Updates.objects.filter(subject=subject.id,level=level.id).order_by("-published_date"):
				recent_updates.append({'info':recent_update})
			if recent_updates:
        			subjects.append({'id':subject.id,'name':subject.name,'recent_updates':recent_updates})
        	if subjects:
        		levels.append({'id':level.id,'name':level.name,'subjects':subjects})
	return render_to_response('recent_updates_level.html',{'levels':levels, 'user':request.user, 'next':request.META['PATH_INFO']})
level_wise_recent_updates = login_required(level_wise_recent_updates)
