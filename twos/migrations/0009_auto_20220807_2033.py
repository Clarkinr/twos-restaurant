# Generated by Django 3.2.14 on 2022-08-07 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twos', '0008_delete_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-booking_date']},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_made',
            new_name='booking_date',
        ),
    ]
