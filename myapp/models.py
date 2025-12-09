from django.db import models
from django.contrib.auth.models import User

class Caretaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    photo = models.FileField(upload_to='caretaker_photos/')
    id_proof = models.FileField(upload_to='photos')
    approval_status = models.CharField(max_length=15, blank=True, null=True)

class Blind_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CARETAKER = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    place = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255)
    photo = models.FileField(upload_to='photos')
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    radius = models.CharField(max_length=15)

class Complaint(models.Model):
    CARETAKER = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=150)
    reply = models.CharField(max_length=15, blank=True, null=True)
    date = models.CharField(max_length=15)

class Feedback(models.Model):
    CARETAKER = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=15, blank=True, null=True)
    date = models.CharField(max_length=15)


class Familiar_Person(models.Model):
    BLIND = models.ForeignKey(User, on_delete=models.CASCADE)
    relation = models.CharField(max_length=15, blank=True, null=True)
    image = models.FileField(upload_to='photos')




