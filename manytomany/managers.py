from django.db import models

class PersonManager(models.Manager):
    def person_membership(self, person_id, membership_id):
        self.get_queryset().person_membership(person_id, membership_id)