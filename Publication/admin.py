from django import forms
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage,Site
#from django.contrib.flatpages.models import FlatPageFlatPage
from tinymce.widgets import TinyMCE
import models

class AuthorpageForm(forms.ModelForm):
   
    class Meta:
        model = models.Author

class TinyMCEAuthorPageAdmin(admin.ModelAdmin):
    form = AuthorpageForm
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEAuthorPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(models.Author, TinyMCEAuthorPageAdmin)
admin.site.register(models.Publisher)
admin.site.register(models.Distributor)
admin.site.register(models.Subject)
admin.site.register(models.Level)
#admin.site.unregister(FlatPage)
#admin.site.unregister(FlatPage)

class BookpageForm(forms.ModelForm):
   
    class Meta:
        model = models.Book

class TinyMCEBookPageAdmin(admin.ModelAdmin):
    list_display   = ('title', 'subject', 'level', 'publisher', 'publication_date')
    list_filter    = ('subject', 'level', 'publisher', 'publication_date')
    ordering       = ('-publication_date',)
    search_fields  = ('title', )
    
    form = BookpageForm
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEBookPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(models.Book,TinyMCEBookPageAdmin)
