# Generated by Django 4.1.7 on 2023-03-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_blogmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='genre',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
