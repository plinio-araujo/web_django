# Generated by Django 4.2.2 on 2023-08-06 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, default='/static/images/perfil/foto-padrao.jpg', upload_to='perfil/foto/'),
        ),
    ]