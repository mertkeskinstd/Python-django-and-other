# Generated by Django 4.2.6 on 2023-10-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="musician",
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
                ("name", models.CharField(max_length=40)),
                ("instrument", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
