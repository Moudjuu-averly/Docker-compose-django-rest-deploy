# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments import highlight

class Image(models.Model):
	owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	url = models.URLField()
	source_url = models.URLField()
	highlighted = models.TextField()

	class Meta:
		ordering = ('created',)
