# Generated by Django 4.1.6 on 2023-04-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0005_alter_studentmodel_beautiful_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='suggestion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
