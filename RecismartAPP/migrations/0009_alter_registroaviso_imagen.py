# Generated by Django 4.1.4 on 2022-12-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0008_delete_imagenaviso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroaviso',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='publicacion'),
        ),
    ]
