from django.db import models
import datetime
# Create your models here.
from .managers import PersonManager




class Person(models.Model):
    name = models.CharField(max_length=128)

    personman = PersonManager()

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    invite_reason = models.CharField(max_length=64)


class PersonMembership(models.Model):
    person_id = models.IntegerField(null=True, blank=True)
    membership_id = models.IntegerField(null=True, blank=True)



class Cases(models.Model):
    name = models.CharField(max_length=128)


class CaseAccessibleToUser(models.Model):
    case = models.ForeignKey(to=Cases, blank=False, null=False, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=False, blank=False)






