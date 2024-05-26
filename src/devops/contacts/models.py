from django.db import models

class Contact(models.Model):
    """Model for adding new contacts"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, default="")
    number = models.IntegerField(default=000)

