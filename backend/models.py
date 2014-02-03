from django.db import models
from django.conf import settings

class Persona(models.Model):
    name = models.CharField(max_length=20)
    contact = models.TextField()
    skills = models.TextField()
    cv = models.FileField(upload_to=settings.FILEBROWSER_DIRECTORY)
    site_name = models.CharField(max_length=200)
    def __unicode__(self):
        return unicode(self.name)
    def count_active_projects(self):
        return self.project_set.all().filter(status=1).count()

class Category(models.Model):
    key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Archived'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    css_class = models.CharField(max_length=20, null=True, default=None)
    main_image_url = models.CharField(max_length=200,null=True, default=None)
    status = models.IntegerField(choices=STATUS_CHOICES)
    author = models.ForeignKey(Persona)
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.name
    class Meda:
        ordering = ['status','name']

class ProjectDetail(models.Model):
    project = models.ForeignKey(Project)
    caption = models.TextField(max_length=200)
    description = models.TextField(max_length=500, null=True, default=None)
    main_image_url = models.CharField(max_length=200,null=True, default=None)
    def __unicode__(self):
        return unicode(self.project) + ' - ' + unicode(self.caption)

class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.FileField(upload_to=settings.FILEBROWSER_DIRECTORY)
    position = models.PositiveSmallIntegerField("Position")
    def __unicode__(self):
        return unicode(self.title)
    class Meta:
        verbose_name_plural = 'Carousel'
        ordering = ['position']
    
class Metadata(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Metadata'

    