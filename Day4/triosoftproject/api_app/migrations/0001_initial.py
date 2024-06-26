# Generated by Django 5.0.6 on 2024-05-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrioCompany',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField(null=True)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT'), ('MOBILE PHONE', 'MOBILE PHONE')], max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
