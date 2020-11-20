# Generated by Django 2.2.13 on 2020-11-18 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_auto_20201116_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Hidden'), (1, 'Visible'), (2, 'Home')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_posts', to='feed.Tag'),
        ),
    ]