from django.db import models
import hashlib
import django.conf
import django.core.mail
import datetime

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Handset(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=255)

class Requester(models.Model):
    email = models.EmailField()

class AndroidSourceRequest(models.Model):
    handset = models.ForeignKey(Handset)
    requester = models.ForeignKey(Requester)
    requester_name = models.CharField(max_length=255)
    request_is_confirmed = models.BooleanField(default=False)
    email_was_sent_on = models.DateTimeField(null=True, default=None)

    def get_email_confirmation_key(self):
        hasher = hashlib.sha1()
        hasher.update(django.conf.settings.SECRET_KEY)
        hasher.update(self.requester.email)
        return hasher.hexdigest()

    def mark_confirmed(self, key):
        correct_key = self.get_email_confirmation_key()
        if key == correct_key:
            self.request_is_confirmed = True

    def send_as_email(self):
        django.core.mail.send_mail(
            'SUBJECT',
            'MESSAGE ' + self.get_email_confirmation_key(), # FIXME: Use a template
            'from-address@example.com',
            ['recipient1@example.com', 'recipient2@example.com'])
        self.email_was_sent_on = datetime.datetime.utcnow()
