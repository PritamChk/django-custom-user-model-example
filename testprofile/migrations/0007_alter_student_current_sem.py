# Generated by Django 4.0.3 on 2022-03-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testprofile', '0006_alter_department_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_sem',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-st'), (2, '2-nd'), (3, '3-rd'), (4, '4-th'), (5, '5-th'), (6, '6-th'), (7, '7-th'), (8, '8-th'), (9, '9-th'), (10, '10-th')], db_index=True, default=1, help_text='Select Your On Going Sem🔢', verbose_name='Choose Sem [1-10]-th'),
        ),
    ]
