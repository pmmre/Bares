from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Tapa(models.Model):
    nombre_tapa = models.CharField(max_length=50, primary_key=True)
    descripcion = models.CharField(max_length=128,null=True)
    votos = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='imagenes_tapa',blank=True)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre_tapa


class Bar(models.Model):
    nombre_bar = models.CharField(max_length=128, primary_key=True)
    descripcion_bar = models.CharField(max_length=128,null=True)
    num_visitas = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    direccion = models.CharField(max_length=250, blank=True)
    #category_name_url = models.CharField(max_length=128,null=True)

    tapas = models.ManyToManyField(Tapa)
    
    def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre_bar)
		super(Bar, self).save(*args, **kwargs)


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.nombre_bar



class UserProfile(models.Model):
	user = models.OneToOneField(User)

	picture = models.ImageField(upload_to='profile_images',blank=True)

	def __unicode__(self):
		return self.user.username

