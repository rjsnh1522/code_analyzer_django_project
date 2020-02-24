from django.db import models

class PersonQuerySet(models.QuerySet):
	def person_membership(self, person_id, membership_id)