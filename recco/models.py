from django.db import models

class Destination(models.Model):
    DestinationID = models.IntegerField(primary_key=True, default=1)
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Region = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)

    def __str__(self):
        return self.City

    class Meta:
        db_table = 'Destination'  # Specify the name of the existing table in your database

class Activity(models.Model):
    ActivityID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    DestinationID = models.ForeignKey(Destination, on_delete=models.CASCADE, db_column='DestinationID')

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Activity'  # Specify the name of the existing table in your database

class Accommodation(models.Model):
    AccommodationID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=50)
    Address = models.CharField(max_length=255)
    DestinationID = models.ForeignKey(Destination, on_delete=models.CASCADE, db_column='DestinationID')

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Accommodation'  # Specify the name of the existing table in your database

