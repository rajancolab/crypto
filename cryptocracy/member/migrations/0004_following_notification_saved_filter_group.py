# Generated by Django 3.1 on 2020-08-27 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
        ('member', '0003_auto_20200827_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved_filter_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('group_id', models.CharField(max_length=20)),
                ('first_argument', models.IntegerField(blank=True, null=True)),
                ('second_argument', models.IntegerField(blank=True, null=True)),
                ('third_argument', models.IntegerField(blank=True, null=True)),
                ('fourth_argument', models.IntegerField(blank=True, null=True)),
                ('fifth_argument', models.IntegerField(blank=True, null=True)),
                ('filter', models.ManyToManyField(related_name='member_saved_filter_group_filter', to='filter.Filter')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('System', 'System'), ('Crypto Signal', 'Crypto Signal'), ('Friend', 'Friend')], max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crypto_asset', models.CharField(max_length=50)),
                ('crypto_ticker', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Muted', 'Muted'), ('All', 'All'), ('Partial', 'Partial')], max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
        ),
    ]
