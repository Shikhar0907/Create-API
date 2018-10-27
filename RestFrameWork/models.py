from django.db import models
from django.conf import settings
# Create your models here.

def  Upload_status_image(instance,filename):
    return("updates/{user}/{filename}".format(user=instance.user,filename=filename))

class Statusqueryset(models.QuerySet):
    pass

class Statusmanager(models.Manager):
    def get_queryset(self):
        return(Statusqueryset(self.model,using=self._db))



class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=Upload_status_image,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = Statusmanager()

    def __str__(self):
        return(str(self.content)[:50])

    class Meta:
        verbose_name = 'Status_post'
        verbose_name_plural = 'Status_posts'