# Generated by Django 4.2.1 on 2023-06-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_polo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="color",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app_polo.color",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="size",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app_polo.size",
            ),
            preserve_default=False,
        ),
    ]