# Generated by Django 4.0.5 on 2022-07-02 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='slud',
            new_name='slug',
        ),
    ]
