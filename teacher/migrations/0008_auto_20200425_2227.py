# Generated by Django 3.0.5 on 2020-04-25 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20200425_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Section'),
        ),
    ]