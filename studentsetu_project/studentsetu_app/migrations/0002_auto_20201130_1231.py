# Generated by Django 2.2.5 on 2020-11-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsetu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]