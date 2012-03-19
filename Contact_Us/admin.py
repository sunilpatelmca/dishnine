from django import forms
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage,Site
import models

admin.site.register(models.Contact_Us)
