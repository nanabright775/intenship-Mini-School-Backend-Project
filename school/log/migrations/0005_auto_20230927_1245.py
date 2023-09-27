# Generated by Django 3.2 on 2023-09-27 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20230926_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='log.grade'),
        ),
    ]