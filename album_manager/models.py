from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=75, null=False)
    country = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=100, null=False)
    year = models.IntegerField(default=1, null=False)
    genre = models.CharField(max_length=50, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_cover = models.ImageField(upload_to='album_images')

    def __str__(self) -> str:
        return self.title
    
