# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from models import *
import settings

def all_books_detail(request):
	subjects=[]
	for subject in Subject.objects.all():
		levels=[]
		for level in Level.objects.filter(subject=subject.id):
			books=[]
			for book in Book.objects.filter(subject=subject.id,level=level.id):
				books.append({'info':book,'authors':book.authors.all(),'distributors':book.distributor.all()})
                        if books:
                                levels.append({'id':level.id,'name':level.name,'books':books})
                if levels:
        		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('publication_subject.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})

def get_book_detail(request, object_id):
        if object_id:
	        get_object_or_404(Book, pk = object_id)
		book_object = Book.objects.filter(id=object_id)
	subjects=[]
	for book in book_object:
        	levels=[]
                books=[]
                books.append({'info':book,'authors':book.authors.all(),'distributors':book.distributor.all()})
                level = book.level
                levels.append({'id':level.id,'name':level.name,'books':books})
                subject = book.subject
		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('publication_subject.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})

def subject_wise_book_detail(request,subject_id):
        get_object_or_404(Subject, pk = subject_id)
	subjects=[]
	for subject in Subject.objects.filter(id=subject_id):
		levels=[]
		for level in Level.objects.filter(subject=subject.id):
			books=[]
			for book in Book.objects.filter(subject=subject.id,level=level.id):
				books.append({'info':book,'authors':book.authors.all(),'distributors':book.distributor.all()})
			if books:
                                levels.append({'id':level.id,'name':level.name,'books':books})
                if levels:
        		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('publication_subject.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})

def level_wise_book_detail(request,level_id):
        get_object_or_404(Level, pk = level_id)
        levels=[]
        for level in Level.objects.filter(id=level_id):
		subjects=[]
		for subject in Subject.objects.filter(level=level.id):
			books=[]
			for book in Book.objects.filter(subject=subject.id,level=level.id):
				books.append({'info':book,'authors':book.authors.all(),'distributors':book.distributor.all()})
			if books:
        			subjects.append({'id':subject.id,'name':subject.name,'books':books})
        	if subjects:
        		levels.append({'id':level.id,'name':level.name,'subjects':subjects})
	return render_to_response('publication_level.html',{'levels':levels, 'user':request.user, 'next':request.META['PATH_INFO']})

def book_detail(request,book_id):
        if book_id:
	        get_object_or_404(Book, pk = book_id)
		book_object = Book.objects.filter(id=book_id)
	subjects=[]
	for book in book_object:
        	levels=[]
                books=[]
                books.append({'info':book,'authors':book.authors.all(),'distributors':book.distributor.all()})
                level = book.level
                levels.append({'id':level.id,'name':level.name,'books':books})
                subject = book.subject
		subjects.append({'id':subject.id,'name':subject.name,'levels':levels})
	return render_to_response('book.html',{'subjects':subjects, 'user':request.user, 'next':request.META['PATH_INFO']})
def author_detail(request,author_id):
        get_object_or_404(Author, pk = author_id)
	author=Author.objects.filter(id=author_id)[0]
	return render_to_response('author.html',{'author':author, 'user':request.user, 'next':request.META['PATH_INFO']})

def publisher_detail(request,publisher_id):
        get_object_or_404(Publisher, pk = publisher_id)
	publisher=Publisher.objects.filter(id=publisher_id)[0]
	return render_to_response('publisher.html',{'publisher':publisher, 'user':request.user, 'next':request.META['PATH_INFO']})

def distributor_detail(request,distributor_id):
        get_object_or_404(Distributor, pk = distributor_id)
	distributor=Distributor.objects.filter(id=distributor_id)[0]
	return render_to_response('distributor.html',{'distributor':distributor, 'user':request.user, 'next':request.META['PATH_INFO']})
