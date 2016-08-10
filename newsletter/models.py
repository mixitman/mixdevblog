from __future__ import unicode_literals

from django.db import models

#   Check the docs for model field types - https://docs.djangoproject.com/en/1.9/ref/models/fields/


class SignUp(models.Model):

    email = models.EmailField()
    full_name = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email

    # def __unicode__(self):
    #     return self.email
