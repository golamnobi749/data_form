# Generated by Django 5.0 on 2023-12-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=15)),
                ('father_name', models.CharField(max_length=15)),
                ('mother_name', models.CharField(max_length=15)),
                ('bangla', models.CharField(max_length=15)),
                ('english', models.CharField(max_length=15)),
                ('math', models.CharField(max_length=15)),
                ('social_science', models.CharField(max_length=15)),
                ('general_science', models.CharField(max_length=15)),
                ('religion', models.CharField(max_length=15)),
                ('point', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('confirm_password', models.CharField(max_length=25)),
                ('text_area', models.CharField(max_length=150)),
            ],
        ),
    ]
