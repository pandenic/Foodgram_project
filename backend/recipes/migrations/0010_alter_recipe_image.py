# Generated by Django 4.2.1 on 2023-06-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(help_text='Содержит фото рецепта', upload_to='../media/', verbose_name='Фото рецепта'),
        ),
    ]
