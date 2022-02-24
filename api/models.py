from django.db import models

class SavedData(models.Model):
    code = models.CharField(null=False, max_length=2, default="ME")
    move = models.CharField(null=False, max_length=2, default="S")