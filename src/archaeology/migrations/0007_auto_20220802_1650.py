# Generated by Django 2.2.24 on 2022-08-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0031_auto_20201107_2241'),
        ('archaeology', '0006_auto_20220801_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrence',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='document',
        ),
        migrations.RemoveField(
            model_name='site',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='site',
            name='document',
        ),
        migrations.AddField(
            model_name='occurrence',
            name='attribute_occurrence',
            field=models.ManyToManyField(blank=True, to='archaeology.AttributeChoice', verbose_name='attribute'),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='document_occurrence',
            field=models.ManyToManyField(blank=True, to='documents.Document', verbose_name='document'),
        ),
        migrations.AddField(
            model_name='site',
            name='attribute_site',
            field=models.ManyToManyField(blank=True, to='archaeology.AttributeChoice', verbose_name='attribute'),
        ),
        migrations.AddField(
            model_name='site',
            name='document_site',
            field=models.ManyToManyField(blank=True, to='documents.Document', verbose_name='document'),
        ),
    ]
