# Generated by Django 4.2 on 2023-04-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_post_curtidas_curtidas'),
    ]

    operations = [
        migrations.AddField(
            model_name='curtidas',
            name='ip_usuario',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
