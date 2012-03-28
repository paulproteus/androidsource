from django.db import models
import hashlib
import django.conf

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

class Handset(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=255)

class Requester(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    email_is_confirmed = models.BooleanField(default=False)

    def get_email_confirmation_key(self):
        hasher = hashlib.sha()
        hasher.update(django.conf.settings.SECRET_KEY)
        hasher.update(self.email)
        return hasher.digest()

class AndroidSourceRequest(models.Model):
    handset = models.ForeignKey(Manufacturer)
    requester = models.ForeignKey(Requester)
