# Generated by Django 2.2.6 on 2019-11-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtapp', '0003_auto_20191013_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='geneLengthList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geneID', models.CharField(default='GL-0000XX', max_length=30)),
                ('gene', models.CharField(default='SOME GENE', max_length=100)),
                ('length', models.IntegerField(default=100)),
            ],
            options={
                'verbose_name_plural': 'Gene-Disease and length',
            },
        ),
        migrations.AlterModelOptions(
            name='genediseaselist',
            options={},
        ),
        migrations.RenameField(
            model_name='genediseaselist',
            old_name='geneDisease',
            new_name='disease',
        ),
        migrations.RemoveField(
            model_name='genediseaselist',
            name='length',
        ),
        migrations.AddField(
            model_name='genediseaselist',
            name='geneID',
            field=models.CharField(default='GL-0000XX', max_length=30),
        ),
    ]
