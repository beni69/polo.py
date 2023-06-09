# Generated by Django 4.2.1 on 2023-06-03 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("TAN", "Tanár"),
                            ("OLD", "Öregdiák"),
                            ("XA", "Leendő NYA"),
                            ("XB", "Leendő 9B"),
                            ("XC", "Leendő 9C"),
                            ("XD", "Leendő 9D"),
                            ("XE", "Leendő NYE"),
                            ("XF", "Leendő NYF"),
                            ("0A", "NYA"),
                            ("0E", "NYE"),
                            ("0F", "NYF"),
                            ("9A", "9A"),
                            ("9B", "9B"),
                            ("9C", "9C"),
                            ("9D", "9D"),
                            ("9E", "9E"),
                            ("9F", "9F"),
                            ("10A", "10A"),
                            ("10B", "10B"),
                            ("10C", "10C"),
                            ("10D", "10D"),
                            ("10E", "10E"),
                            ("10F", "10F"),
                            ("11A", "11A"),
                            ("11B", "11B"),
                            ("11C", "11C"),
                            ("11D", "11D"),
                            ("11E", "11E"),
                            ("11F", "11F"),
                            ("12A", "12A"),
                            ("12B", "12B"),
                            ("12C", "12C"),
                            ("12D", "12D"),
                            ("12E", "12E"),
                            ("12F", "12F"),
                        ],
                        max_length=3,
                    ),
                ),
                ("teacher", models.CharField(max_length=50)),
            ],
        ),
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
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=20)),
                ("link", models.URLField()),
                ("image", models.URLField()),
                ("colors", models.ManyToManyField(to="app_polo.color")),
                ("sizes", models.ManyToManyField(to="app_polo.size")),
            ],
        ),
        migrations.CreateModel(
            name="PoloUser",
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
                (
                    "osztaly",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app_polo.class",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_polo.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_polo.polouser",
                    ),
                ),
            ],
        ),
    ]
