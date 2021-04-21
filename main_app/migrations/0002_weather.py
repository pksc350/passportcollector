# Generated by Django 3.2 on 2021-04-21 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weather', models.CharField(choices=[('S', 'Sunny'), ('R', 'Rainy'), ('C', 'Cloudy'), ('W', 'Windy')], default='S', max_length=1)),
                ('stamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stamp')),
            ],
        ),
    ]
