# Generated by Django 4.1 on 2022-08-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0033_emailpool_alter_aiworkshop_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdisplay',
            name='branch3',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='branch4',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='branch5',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='email3',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='email4',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='email5',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='id3',
            field=models.FileField(blank=True, null=True, upload_to='ProjectDisplay/'),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='id4',
            field=models.FileField(blank=True, null=True, upload_to='ProjectDisplay/'),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='id5',
            field=models.FileField(blank=True, null=True, upload_to='ProjectDisplay/'),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='name3',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='name4',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='name5',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='phone3',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='phone4',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='phone5',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='rollno3',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='rollno4',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='rollno5',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='semester3',
            field=models.CharField(blank=True, default=' ', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='semester4',
            field=models.CharField(blank=True, default=' ', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='projectdisplay',
            name='semester5',
            field=models.CharField(blank=True, default=' ', max_length=5, null=True),
        ),
    ]
