# Generated by Django 4.0.4 on 2022-05-17 19:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PanelUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                ("name", models.CharField(max_length=60, verbose_name="Name")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "date_joined",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Date Joined"
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Active"), (2, "Blocked")],
                        default=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="Is Superuser"),
                ),
            ],
            options={
                "verbose_name": "PanelUser",
                "verbose_name_plural": "PanelUsers",
                "db_table": "panel_user",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                ("name", models.CharField(max_length=60, verbose_name="Name")),
                (
                    "country_code",
                    models.CharField(max_length=10, verbose_name="Country Code"),
                ),
                ("latitude", models.FloatField(verbose_name="Latitude")),
                ("longitude", models.FloatField(verbose_name="Longitude")),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
                "db_table": "city",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="DynamicConfigParameter",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "key",
                    models.CharField(max_length=100, unique=True, verbose_name="Key"),
                ),
                ("value", models.TextField(null=True, verbose_name="Value")),
            ],
            options={
                "verbose_name": "Dynamic Config Parameter",
                "verbose_name_plural": "Dynamic Config Parameters",
                "db_table": "dynamic_config_parameter",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Results",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "start_date",
                    models.DateField(max_length=60, verbose_name="Start date"),
                ),
                ("end_date", models.DateField(max_length=60, verbose_name="End date")),
                ("distance", models.PositiveIntegerField(verbose_name="Distance")),
                ("date", models.DateField(max_length=60, verbose_name="Date")),
                (
                    "earthquake",
                    models.CharField(
                        max_length=100, verbose_name="Earthquake Description"
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="city_results",
                        to="domain.city",
                        verbose_name="City",
                    ),
                ),
            ],
            options={
                "verbose_name": "Result",
                "verbose_name_plural": "Results",
                "db_table": "result",
                "ordering": ["distance"],
            },
        ),
    ]
