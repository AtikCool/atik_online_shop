# Generated by Django 4.2.4 on 2023-08-28 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_rename_backet_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='prduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='main.product'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
