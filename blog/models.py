from uuid import uuid4
from django.db import models
from blogish import settings

def upload_location(instance, filename):
    ext=filename.split('.')[-1]
    file_path= 'news_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)

    )
    return file_path

class PagesModel(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null= True)
    image = models.ImageField(upload_to=upload_location , null = True, blank = True)
    created_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.title)
    
    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url