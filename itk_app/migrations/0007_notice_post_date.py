# Generated by Django 2.2.7 on 2019-12-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itk_app', '0006_auto_20191202_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='post_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
