from django.db import models

class Slra(models.Model):
    upload = models.FileField(upload_to='uploads/')
    summary = models.CharField(max_length=200)
