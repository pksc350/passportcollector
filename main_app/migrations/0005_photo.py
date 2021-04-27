# Generated by Django 3.2 on 2021-04-22 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210421_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('stamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stamp')),
            ],
        ),
    ]
