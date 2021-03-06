# Generated by Django 2.2.6 on 2019-11-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categoria', models.IntegerField(choices=[(0, 'Geral'), (1, 'Banheiro'), (2, 'Cozinha'), (3, 'Quarto'), (4, 'Sala'), (5, 'Área externa')], default=0)),
            ],
        ),
    ]
