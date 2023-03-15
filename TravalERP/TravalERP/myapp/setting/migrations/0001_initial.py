# Generated by Django 4.1.7 on 2023-03-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(db_column='AGENT_NAME', max_length=100)),
                ('agent_tel', models.CharField(db_column='AGENT_TEL', max_length=100)),
                ('agent_type', models.CharField(db_column='AGENT_TYPE', max_length=100)),
                ('use_yn', models.CharField(db_column='USE_YN', max_length=100)),
                ('entry_id', models.CharField(db_column='ENTRY_ID', max_length=20)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('updat_id', models.CharField(blank=True, db_column='UPDAT_ID', max_length=20, null=True)),
                ('updat_date', models.DateTimeField(blank=True, db_column='UPDAT_DATE', null=True)),
            ],
            options={
                'db_table': 'agent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(db_column='AGENT_NAME', max_length=100)),
                ('manager_name', models.CharField(db_column='MANAGER_NAME', max_length=100)),
                ('manager_tel', models.CharField(db_column='MANAGER_TEL', max_length=20)),
                ('type', models.CharField(db_column='TYPE', max_length=100)),
                ('manager_hp', models.CharField(db_column='MANAGER_HP', max_length=100)),
                ('manager_messenger', models.CharField(db_column='MANAGER_MESSENGER', max_length=100)),
                ('manager_email', models.CharField(db_column='MANAGER_EMAIL', max_length=100)),
                ('manager_remark', models.TextField(db_column='MANAGER_REMARK', max_length=1000)),
                ('use_yn', models.CharField(db_column='USE_YN', max_length=100)),
                ('entry_id', models.CharField(db_column='ENTRY_ID', max_length=20)),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE')),
                ('updat_id', models.CharField(blank=True, db_column='UPDAT_ID', max_length=20, null=True)),
                ('updat_date', models.DateTimeField(blank=True, db_column='UPDAT_DATE', null=True)),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
    ]
