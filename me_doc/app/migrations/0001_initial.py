# Generated by Django 4.2.5 on 2023-10-31 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("eid", models.CharField(max_length=20)),
                ("ename", models.CharField(max_length=100)),
                ("eemail", models.EmailField(max_length=254)),
                ("econtact", models.CharField(max_length=15)),
            ],
            options={"db_table": "patient",},
        ),
    ]
