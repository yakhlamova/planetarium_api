# Generated by Django 4.2.4 on 2023-08-10 22:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("planeyarium", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservation",
            options={"ordering": ["-created_at"]},
        ),
    ]
