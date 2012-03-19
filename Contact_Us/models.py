from django.db import models

class Contact_Us(models.Model):
     name = models.CharField(max_length=40,help_text='Maximum 40 characters.')
     address = models.CharField(max_length=50)
     city = models.CharField(max_length=60)
     state_province = models.CharField(max_length=30)
     country = models.CharField(max_length=50)
     website = models.CharField(max_length=100,blank=True,help_text='(Ex. : http://www.dishnine.com)')
     email = models.EmailField(blank=True)
     phone = models.CharField(max_length=20,blank=True,help_text='(Ex. : +91 079 22205951)')
     mobile = models.CharField(max_length=20,blank=True,help_text='(Ex. : +91 9879996878)')
     fax = models.CharField(max_length=30,blank=True)
     
     class Meta:
	     verbose_name_plural = "Contact Us"

     class Admin:
	     pass

     def __unicode__(self):
	     return '%s'%(self.name,)
