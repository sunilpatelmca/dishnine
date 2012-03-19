from django.template import Library,Node
from django.http import HttpResponse
from django.db.models import get_model
import settings
import base64
register = Library()

def get_file(FileName):
     print "@@@@@@@@@@@@ file @@@@@@@@@@@@@@ ",FileName._get_name()
     return FileName.url

register.simple_tag(get_file)
