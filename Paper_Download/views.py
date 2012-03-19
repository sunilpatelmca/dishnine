# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from models import *
import settings
from django.contrib.auth.decorators import login_required

def paper_download(request):
	subjects=[]
	for subject in Subject.objects.all():
		levels=[]
		for level in Level.objects.filter(subject=subject.id):
			paper_downloads=[]
			for paper_download in Paper_Download.objects.filter(subject=subject.id,level=level.id):
				paper_downloads.append({'info':paper_download})
			if paper_downloads:
        			levels.append({'id':level.id,'name':level.name,'paper_downloads':paper_downloads})
        	if levels:
        		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('paper_download.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
paper_download = login_required(paper_download)

def get_paper_download(request, object_id):
	if object_id:
	        get_object_or_404(Paper_Download, pk = object_id)
		paper_download_object = Paper_Download.objects.filter(id=object_id)
	subjects=[]
	for paper_download in paper_download_object:
		levels=[]
		paper_downloads=[]		
		paper_downloads.append({'info':paper_download})
		level = paper_download.level
		levels.append({'id':level.id,'name':level.name,'paper_downloads':paper_downloads})
		subject = paper_download.subject
		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('paper_download.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
get_paper_download = login_required(get_paper_download)

def subject_wise_paper_download(request,subject_id):
	if subject_id:
	        get_object_or_404(Subject, pk = subject_id)
		subject_objects=Subject.objects.filter(id=subject_id)	
	else:
		subject_objects=Subject.objects.all()	
	subjects=[]
	for subject in subject_objects:
		levels=[]
		for level in Level.objects.filter(subject=subject.id):
			paper_downloads=[]
			for paper_download in Paper_Download.objects.filter(subject=subject.id,level=level.id):
				paper_downloads.append({'info':paper_download})
			if paper_downloads:
        			levels.append({'id':level.id,'name':level.name,'paper_downloads':paper_downloads})
        	if levels:
        		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('paper_download_subject.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
subject_wise_paper_download = login_required(subject_wise_paper_download)

def level_wise_paper_download(request,level_id):
        get_object_or_404(Level, pk = level_id)
        levels=[]
        for level in Level.objects.filter(id=level_id):
		subjects=[]
		for subject in Subject.objects.filter(level=level.id):
			paper_downloads=[]
			for paper_download in Paper_Download.objects.filter(subject=subject.id,level=level.id):
				paper_downloads.append({'info':paper_download})
			if paper_downloads:
        			subjects.append({'id':subject.id,'name':subject.name,'paper_downloads':paper_downloads})
        	if subjects:
        		levels.append({'id':level.id,'name':level.name,'subjects':subjects})
	return render_to_response('paper_download_level.html',{'levels':levels, 'user':request.user, 'next':request.META['PATH_INFO']})
level_wise_paper_download = login_required(level_wise_paper_download)
