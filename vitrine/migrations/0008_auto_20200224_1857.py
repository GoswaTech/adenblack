# Generated by Django 3.0.3 on 2020-02-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0007_auto_20200224_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artcompositing',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='artmapping',
            name='poster',
        ),
    ]