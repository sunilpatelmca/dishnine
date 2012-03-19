from django.template import Library,Node
from django.http import HttpResponse
from django.db.models import get_model
import settings
import base64
register = Library()

def get_image(FileName):
     return FileName.url

register.simple_tag(get_image)
