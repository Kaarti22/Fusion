# Generated by Django 3.1.5 on 2024-04-11 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '__first__'),
        ('otheracademic', '0003_leaveformtable_hod'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeavePG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=100)),
                ('discipline', models.CharField(max_length=100)),
                ('Semester', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('date_of_application', models.DateField()),
                ('upload_file', models.FileField(upload_to='leave_doc')),
                ('address', models.CharField(max_length=100)),
                ('purpose', models.TextField()),
                ('leave_type', models.CharField(choices=[('Casual', 'Casual'), ('Medical', 'Medical'), ('Vacation', 'Vacation'), ('Duty', 'Duty')], max_length=20)),
                ('mobile_no', models.CharField(max_length=100)),
                ('parent_mobile_no', models.CharField(max_length=100)),
                ('alt_mobile_no', models.CharField(max_length=100)),
                ('ta_approved', models.BooleanField()),
                ('ta_rejected', models.BooleanField()),
                ('hod_approved', models.BooleanField()),
                ('hod_rejected', models.BooleanField()),
                # ('ta_supervisor', models.CharField(max_length=100)),
                # ('hod', models.CharField(max_length=100)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'LeavePG',
            },
        ),
    ]
