# Generated by Django 4.2.6 on 2023-12-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='dept_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept'),
        ),
    ]
