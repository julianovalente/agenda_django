# Generated by Django 4.0.1 on 2022-06-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contato_ddd1_alter_contato_telefone1'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='ddd2',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='contato',
            name='ddd3',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='contato',
            name='telefone2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contato',
            name='telefone3',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='contato',
            name='ddd1',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone1',
            field=models.CharField(default='', max_length=10),
        ),
    ]
