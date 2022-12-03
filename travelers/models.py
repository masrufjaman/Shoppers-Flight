from django.db import models

class TravelersPost(models.Model):
    flight_date = models.DateField()
    arrival_date = models.DateField()
    destination_country = models.CharField(max_length=50)
    origin_country = models.CharField(max_length=50)
    passport_no = models.IntegerField()
    ticket_no = models.IntegerField()
    airlines_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_no = models.IntegerField()
    class Meta:
        db_table="flightdetails"
        


class Traveler(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
