# Generated by Django 4.0.1 on 2022-06-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_telefone_contato_telefone1'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='ddd1',
            field=models.CharField(default='00', max_length=2),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone1',
            field=models.CharField(max_length=10),
        ),
    ]
