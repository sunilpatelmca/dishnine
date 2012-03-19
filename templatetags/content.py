from django.template import Library,Node
from django.http import HttpResponse
from django.db.models import get_model

register = Library()

def get_content(content):
    
    return HttpResponse(content,mimetype="text/html")._get_content()
    
register.simple_tag(get_content)
