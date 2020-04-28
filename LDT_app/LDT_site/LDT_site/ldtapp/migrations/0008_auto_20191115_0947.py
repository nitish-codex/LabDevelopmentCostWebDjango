# Generated by Django 2.2.6 on 2019-11-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtapp', '0007_remove_genelengthlist_geneid'),
    ]

    operations = [
        migrations.CreateModel(
            name='hybridProbesCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numProbeslim', models.IntegerField(default=50)),
                ('pricesInEUR', models.FloatField(default=300)),
            ],
            options={
                'verbose_name_plural': 'NumberOfProbes & its cost',
            },
        ),
        migrations.RemoveField(
            model_name='variables',
            name='hybridKitCost',
        ),
        migrations.AddField(
            model_name='variables',
            name='eurToDollerConFact',
            field=models.FloatField(default=100),
        ),
    ]
