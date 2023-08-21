# Generated by Django 4.2.4 on 2023-08-21 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "sku",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Batch",
            fields=[
                (
                    "reference",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("available_qty", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="batch_managing.product",
                    ),
                ),
            ],
        ),
    ]
