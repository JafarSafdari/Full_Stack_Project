# Generated by Django 4.0.4 on 2022-05-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_lessee_carreg_remove_lessee_useremail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
