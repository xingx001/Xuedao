# Generated by Django 3.0.5 on 2020-06-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_recommends_col_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommends',
            name='col_count',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
