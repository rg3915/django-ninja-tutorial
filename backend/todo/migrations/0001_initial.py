# Generated by Django 3.2.4 on 2021-06-04 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='data')),
                ('is_done', models.BooleanField(default=False, verbose_name='pronto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'todo',
                'verbose_name_plural': 'todos',
                'ordering': ('title',),
            },
        ),
    ]
