# Generated by Django 4.1.7 on 2023-03-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(default='', max_length=25, verbose_name='Name')),
                ('employee_designation', models.CharField(default='', max_length=30, verbose_name='Designation')),
                ('contact_number', models.IntegerField(default='', verbose_name='Contact Number')),
            ],
        ),
    ]