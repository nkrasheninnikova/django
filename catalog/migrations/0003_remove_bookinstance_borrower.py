# Generated by Django 3.2.25 on 2024-11-20 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='borrower',
        ),
    ]