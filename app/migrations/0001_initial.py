# Generated by Django 4.2.6 on 2023-12-08 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('dept_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
