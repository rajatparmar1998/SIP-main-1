# Generated by Django 3.0.4 on 2021-01-25 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20210125_1341'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='addcart',
        ),
        migrations.DeleteModel(
            name='sub_category',
        ),
    ]