from django import forms
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage,Site
#from django.contrib.flatpages.models import FlatPageFlatPage
from tinymce.widgets import TinyMCE
import models

class TermspageForm(forms.ModelForm):
   
    class Meta:
        model = models.Terms_Service

class TinyMCETermsPageAdmin(admin.ModelAdmin):
    form = TermspageForm
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCETermsPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(models.Terms_Service, TinyMCETermsPageAdmin)
