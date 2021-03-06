# Generated by Django 2.2.11 on 2020-04-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0005_auto_20200404_2359"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthentry", name="age", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="healthentry",
            name="cough",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="healthentry",
            name="difficult_breathing",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="healthentry",
            name="fever",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="healthentry",
            name="gender",
            field=models.CharField(
                choices=[("Male", "M"), ("Female", "F")], default="M", max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="healthentry",
            name="self_quarantine",
            field=models.BooleanField(default=False),
        ),
    ]
