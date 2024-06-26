# Generated by Django 4.2.4 on 2024-04-04 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recco", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Accommodation",
            fields=[
                (
                    "AccommodationID",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Type", models.CharField(max_length=50)),
                ("Address", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "Accommodation",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("ImageID", models.AutoField(primary_key=True, serialize=False)),
                ("ImagePath", models.CharField(max_length=255)),
                (
                    "AccommodationID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recco.accommodation",
                    ),
                ),
            ],
            options={
                "db_table": "Image",
            },
        ),
        migrations.RemoveField(
            model_name="tripoptionsactivity",
            name="activity_id",
        ),
        migrations.RemoveField(
            model_name="tripoptionsactivity",
            name="optionid",
        ),
        migrations.RenameField(
            model_name="activity",
            old_name="description",
            new_name="Description",
        ),
        migrations.RenameField(
            model_name="activity",
            old_name="name",
            new_name="Name",
        ),
        migrations.RenameField(
            model_name="destination",
            old_name="city",
            new_name="City",
        ),
        migrations.RenameField(
            model_name="destination",
            old_name="country",
            new_name="Country",
        ),
        migrations.RenameField(
            model_name="destination",
            old_name="description",
            new_name="Description",
        ),
        migrations.RenameField(
            model_name="destination",
            old_name="region",
            new_name="Region",
        ),
        migrations.RemoveField(
            model_name="activity",
            name="cost",
        ),
        migrations.RemoveField(
            model_name="activity",
            name="duration",
        ),
        migrations.AlterField(
            model_name="activity",
            name="ActivityID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="activity",
            name="DestinationID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="recco.destination"
            ),
        ),
        migrations.AlterField(
            model_name="destination",
            name="DestinationID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name="TripOptions",
        ),
        migrations.DeleteModel(
            name="TripOptionsActivity",
        ),
        migrations.AddField(
            model_name="image",
            name="ActivityID",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="recco.activity",
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="DestinationID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="recco.destination"
            ),
        ),
        migrations.AddField(
            model_name="accommodation",
            name="DestinationID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="recco.destination"
            ),
        ),
    ]
