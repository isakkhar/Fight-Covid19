# Generated by Django 2.2.11 on 2020-04-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0009_auto_20200406_1836"),
    ]

    operations = [
        migrations.AddField(
            model_name="healthentry",
            name="unique_id",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]