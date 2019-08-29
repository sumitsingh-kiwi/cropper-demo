from django.db import models

# Create your models here.


class Attachment(models. Model):
    document = models.ImageField()

    def __str__(self):
        return self.document.name