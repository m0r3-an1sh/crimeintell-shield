# Generated by Django 4.1.2 on 2023-01-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_blog_descimagelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
