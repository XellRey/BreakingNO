# Generated by Django 4.2.7 on 2023-11-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.CharField(default='Under Consideration', max_length=50, null=True),
        ),
    ]
