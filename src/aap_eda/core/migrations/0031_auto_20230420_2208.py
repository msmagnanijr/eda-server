# Generated by Django 3.2.18 on 2023-04-20 22:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0030_activation_rulebook_fields"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="auditaction",
            options={"ordering": ("-fired_at", "-rule_fired_at")},
        ),
        migrations.AlterModelOptions(
            name="auditevent",
            options={"ordering": ("-rule_fired_at", "-received_at")},
        ),
        migrations.AlterModelOptions(
            name="auditrule",
            options={"ordering": ("-fired_at",)},
        ),
    ]