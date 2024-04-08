# Generated by Django 4.2.11 on 2024-04-07 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('CR', 'Created'), ('OP', 'Open'), ('TL', 'Tallying'), ('CL', 'Closed')], default='CR', max_length=2)),
                ('results', models.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'indexes': [models.Index(fields=['modified'], name='ranked_choi_modifie_9e4cbf_idx')],
            },
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_candidates', models.JSONField()),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranked_choice.vote')),
            ],
        ),
    ]
