# Generated by Django 2.2.6 on 2019-11-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0011_produtocarrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='produto',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produto',
            field=models.ManyToManyField(to='loja.Produto'),
        ),
    ]
