# Generated by Django 2.2.6 on 2019-11-22 13:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loja', '0006_auto_20191122_1026'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProdutoCliente',
            new_name='Carrinho',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='comprado',
        ),
    ]
