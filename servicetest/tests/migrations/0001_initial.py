# Generated by Django 4.1.4 on 2022-12-15 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kits_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riddle_text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('kits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.kits')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('riddle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.riddle')),
            ],
        ),
    ]