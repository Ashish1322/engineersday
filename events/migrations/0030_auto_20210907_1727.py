# Generated by Django 3.1.5 on 2021-09-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_auto_20210907_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiworkshop',
            name='id1',
            field=models.FileField(upload_to='Aiworkshop/'),
        ),
    ]