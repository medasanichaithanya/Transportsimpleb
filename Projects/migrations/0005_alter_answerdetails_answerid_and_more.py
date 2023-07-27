# Generated by Django 4.2.3 on 2023-07-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_answerdetails_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerdetails',
            name='answerid',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='answerdetails',
            name='likescount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answerdetails',
            name='questionid',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='answerdetails',
            name='userid',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='questiondetails',
            name='questionid',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='questiondetails',
            name='userid',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]