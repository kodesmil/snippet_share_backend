# Generated by Django 2.1.7 on 2019-06-02 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20190601_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='snippets.Snippet'),
        ),
    ]