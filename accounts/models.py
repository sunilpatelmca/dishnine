from django.db import models
from Publication.models import Author

class Terms_Service(models.Model):

    title = models.CharField(max_length=50,help_text='Maximum 50 characters.')
    content = models.TextField()

    class Meta:
	    verbose_name_plural = "Registration Terms"


    class Admin:
	    pass

    def __unicode__(self):
	    return self.title




