# Generated by Django 4.2.3 on 2023-09-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='profileImgUrl',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='token',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
