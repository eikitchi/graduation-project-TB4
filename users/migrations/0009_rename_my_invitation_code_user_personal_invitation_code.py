# Generated by Django 4.2.5 on 2023-10-01 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_my_invitation_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='my_invitation_code',
            new_name='personal_invitation_code',
        ),
    ]
