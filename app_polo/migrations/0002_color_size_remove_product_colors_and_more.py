# Generated by Django 4.2.1 on 2023-05-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_polo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, unique=True)),
                ("hex", models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name="product",
            name="colors",
        ),
        migrations.RemoveField(
            model_name="product",
            name="sizes",
        ),
        migrations.AddField(
            model_name="product",
            name="colors",
            field=models.ManyToManyField(to="app_polo.color"),
        ),
        migrations.AddField(
            model_name="product",
            name="sizes",
            field=models.ManyToManyField(to="app_polo.size"),
        ),
    ]
