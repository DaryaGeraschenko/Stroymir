# Generated by Django 4.0.5 on 2022-08-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tovar', '0007_remove_tovarn_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovarn',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
