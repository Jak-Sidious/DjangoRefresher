# Generated by Django 2.2.7 on 2019-11-14 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_step_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
