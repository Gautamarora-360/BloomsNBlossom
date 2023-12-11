from django.db import models
# blog/models.py


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    heading0 = models.CharField(max_length=500, default="")
    content_heading0 = models.CharField(max_length=5000, default="")
    heading1 = models.CharField(max_length=500, default="")
    content_heading1 = models.CharField(max_length=5000, default="")
    heading2 = models.CharField(max_length=500, default="")
    content_heading2 = models.CharField(max_length=5000, default="")
    publishing_date = models.DateField()
    author = models.CharField(max_length=100, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title