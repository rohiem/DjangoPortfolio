from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
# Create your models here.
    
class Project(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField( upload_to="vlog-media")
    video = EmbedVideoField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=False)
    desc=models.CharField(max_length=90)
    pinned=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    belong=models.ForeignKey(Project, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image-project")
    desc=models.TextField( max_length=1000)
    def __str__(self):
        return str(self.id)+"  "+self.belong.title

