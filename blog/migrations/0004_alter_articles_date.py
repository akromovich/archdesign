# Generated by Django 4.0.2 on 2022-03-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_text_alter_post_text_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]