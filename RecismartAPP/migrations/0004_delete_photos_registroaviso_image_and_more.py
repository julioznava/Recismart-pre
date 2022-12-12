# Generated by Django 4.1.4 on 2022-12-12 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0003_photos_alter_registroaviso_fecha_publicacion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='photos',
        ),
        migrations.AddField(
            model_name='registroaviso',
            name='image',
            field=models.ImageField(null=True, upload_to='Portafolio/'),
        ),
        migrations.AlterField(
            model_name='registroaviso',
            name='Fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 1, 17, 2, 895847, tzinfo=datetime.timezone.utc)),
        ),
    ]
