# Generated by Django 4.1.4 on 2022-12-24 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_cv_pdf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CV',
        ),
    ]