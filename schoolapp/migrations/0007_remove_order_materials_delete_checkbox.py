# Generated by Django 4.2.3 on 2023-10-09 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0006_alter_order_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='materials',
        ),
        migrations.DeleteModel(
            name='Checkbox',
        ),
    ]
