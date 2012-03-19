from django.db import models

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=50,help_text='Maximum 50 characters.')
    photo = models.ImageField( height_field = 'photo_height',
                                width_field = 'photo_width',
                                upload_to = '.',
                                blank = True, null = True, )
    content = models.TextField()
#    photo_height = models.IntegerField(blank = True, null = True, )
#    photo_width = models.IntegerField(blank = True, null = True, )
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
	    verbose_name_plural = "Author"

    class Admin:
	list_display   = ('name')
        search_fields  = ('name',)

    def __unicode__(self):
	    return "%s %s"%(self.salutation,self.name)

class Publisher(models.Model):
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
	verbose_name_plural = "Publisher"

     def __unicode__(self):
	return self.name

class Distributor(models.Model):

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
	     verbose_name_plural = "Distributor"

     def __unicode__(self):
	     return self.name

class Subject(models.Model):
    
     name = models.CharField(max_length=120,help_text='Maximum 120 characters.')

     class Meta:
	    verbose_name_plural = "Subject"

     def __unicode__(self):
	    return self.name

class Level(models.Model):
    
     name = models.CharField(max_length=10,help_text='Maximum 10 characters.')
     subject = models.ForeignKey('Subject')

     class Meta:
	    verbose_name_plural = "Level"

     def __unicode__(self):
	    return "%s - [%s]"%(self.name,self.subject.name)

class Book(models.Model):

    title = models.CharField(max_length=50,help_text='Maximum 50 characters.')
    subject = models.ForeignKey('Subject')
    level = models.ForeignKey('Level')
    photo = models.ImageField( height_field = 'photo_height',
                                width_field = 'photo_width',
                                upload_to = '.',
                                blank = True, null = True, )
#    photo_height = models.IntegerField(blank = True, null = True, )
#    photo_width = models.IntegerField(blank = True, null = True, )
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    distributor = models.ManyToManyField(Distributor)
    publication_date = models.DateField()
    content = models.TextField()

    class Meta:
	    verbose_name_plural = "Book"

#    class Admin:
#	list_display   = ('title', 'publisher', 'publication_date')
#        list_filter    = ('publisher', 'publication_date')
#        ordering       = ('-publication_date',)
#        search_fields  = ('title',)

    def __unicode__(self):
	    return "%s [%s - %s]"%(self.title,self.subject.name,self.level.name)



