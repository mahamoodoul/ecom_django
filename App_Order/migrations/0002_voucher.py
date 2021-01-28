# Generated by Django 3.1.4 on 2021-01-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_name', models.CharField(max_length=264)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
