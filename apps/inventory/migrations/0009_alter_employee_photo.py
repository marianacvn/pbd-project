# Generated by Django 4.0.4 on 2022-05-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_employee_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='foto'),
        ),
    ]