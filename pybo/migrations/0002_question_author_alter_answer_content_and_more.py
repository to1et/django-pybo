# Generated by Django 4.1.7 on 2023-02-24 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pybo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="answer",
            name="content",
            field=models.TextField(verbose_name="답변 내용"),
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.TextField(verbose_name="내용"),
        ),
        migrations.AlterField(
            model_name="question",
            name="create_date",
            field=models.DateTimeField(verbose_name="생성일"),
        ),
        migrations.AlterField(
            model_name="question",
            name="subject",
            field=models.CharField(max_length=200, verbose_name="제목"),
        ),
    ]
