from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12)
    email = models.CharField(max_length =100)
    desc = models.CharField(max_length =150)

    def __str__(self):
        return (self.name +". Note : "+self.desc)