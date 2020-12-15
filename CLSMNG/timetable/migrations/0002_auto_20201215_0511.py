# Generated by Django 3.1.4 on 2020-12-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('userID', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('data', models.JSONField(null=True)),
            ],
            options={
                'db_table': 'timetable',
            },
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='申请时间',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='申请理由',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='FeedBack',
        ),
        migrations.DeleteModel(
            name='order_select1',
        ),
        migrations.DeleteModel(
            name='order_select2',
        ),
        migrations.DeleteModel(
            name='OrderModel',
        ),
        migrations.DeleteModel(
            name='select',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
