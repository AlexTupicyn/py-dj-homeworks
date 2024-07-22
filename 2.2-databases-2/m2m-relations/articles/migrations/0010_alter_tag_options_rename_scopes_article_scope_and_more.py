# Generated by Django 5.0.1 on 2024-01-28 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_rename_scope_article_scopes_alter_scope_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='scope',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
    ]