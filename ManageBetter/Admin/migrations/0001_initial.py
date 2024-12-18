# Generated by Django 5.1 on 2024-12-15 09:00

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolid', models.IntegerField(default=1)),
                ('schoolname', models.CharField(default='-', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=1000)),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_classes', to='Admin.schools')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=1)),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_students', to='Admin.schools')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='Admin.user')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.IntegerField(default=0)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classe_grades', to='Admin.classes')),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_grades', to='Admin.schools')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_grades', to='Admin.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_teachers', to='Admin.schools')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='Admin.user')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='Admin.teacher'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_admin', to='Admin.schools')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='Admin.user')),
            ],
        ),
    ]
