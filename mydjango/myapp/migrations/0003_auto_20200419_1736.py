# Generated by Django 3.0.5 on 2020-04-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200418_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='zhishi',
            field=models.CharField(db_column='类型', max_length=128),
        ),
    ]
