# Generated by Django 4.2.4 on 2023-08-11 00:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("planeyarium", "0002_alter_reservation_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="astronomyshow",
            options={"ordering": ["title"]},
        ),
        migrations.AlterModelOptions(
            name="showsession",
            options={"ordering": ["-show_time"]},
        ),
        migrations.AlterModelOptions(
            name="ticket",
            options={"ordering": ["row", "seat"]},
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("show_session", "row", "seat")},
        ),
    ]
