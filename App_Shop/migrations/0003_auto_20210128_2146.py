# Generated by Django 3.1.4 on 2021-01-28 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_MultiVendor', '0003_vendorprofile_is_vendor'),
        ('App_Shop', '0002_product_shop_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shop_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_info', to='App_MultiVendor.vendorprofile'),
        ),
    ]
