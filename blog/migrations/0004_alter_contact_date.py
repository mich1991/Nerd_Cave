# Generated by Django 4.1.5 on 2023-01-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]