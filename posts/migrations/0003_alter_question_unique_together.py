# Generated by Django 3.2 on 2021-06-02 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_community_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('title', 'content')},
        ),
    ]
