# Generated by Django 5.0.7 on 2024-11-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_contactmessage_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('user_ip', models.CharField(max_length=100)),
                ('user_agent', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
