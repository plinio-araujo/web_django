# Generated by Django 4.2.2 on 2023-08-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, default='images/perfil/foto-padrao.jpg', upload_to='perfil/foto/'),
        ),
    ]
