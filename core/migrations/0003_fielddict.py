# Generated by Django 4.0.4 on 2022-06-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_entry_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldDict',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data', models.TextField()),
            ],
        ),
    ]