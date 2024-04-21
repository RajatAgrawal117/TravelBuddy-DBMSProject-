# Generated by Django 5.0.3 on 2024-04-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recco", "0004_alter_accommodation_destinationid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accommodation",
            name="AccommodationID",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="activity",
            name="ActivityID",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="destination",
            name="DestinationID",
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="image",
            name="ImageID",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
