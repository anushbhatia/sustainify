# Generated by Django 3.2.7 on 2021-10-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='pincode',
            field=models.CharField(max_length=10,blank=True, null=True),
        ),
    ]
