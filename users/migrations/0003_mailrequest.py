# Generated by Django 5.2.1 on 2025-06-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_must_change_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='pls enter your email', max_length=254, verbose_name='email')),
                ('message', models.TextField(help_text='enter your name.', verbose_name='message')),
            ],
        ),
    ]
