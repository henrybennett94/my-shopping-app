# Generated by Django 4.2.14 on 2024-08-02 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_alter_shoppinglist_shop_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='temp_shop_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.groceryitem'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='shop_item',
            field=models.CharField(max_length=100),
        ),
    ]
