# Generated by Django 3.1 on 2020-09-07 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20200827_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_member', to='member.member'),
        ),
    ]
