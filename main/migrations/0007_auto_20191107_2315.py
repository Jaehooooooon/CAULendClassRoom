# Generated by Django 2.2.6 on 2019-11-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191107_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='building_no',
            field=models.ForeignKey(db_column='building_no_id', on_delete=django.db.models.deletion.CASCADE, to='main.Building'),
        ),
    ]
