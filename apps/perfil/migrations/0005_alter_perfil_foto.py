# Generated by Django 4.2.2 on 2023-08-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, upload_to='perfil/foto/'),
        ),
    ]
