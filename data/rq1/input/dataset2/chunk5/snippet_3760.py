#Source: https://stackoverflow.com/questions/54114678/how-to-fix-argument-must-be-a-string-typeerror
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[('0', 'Yes'), ('1', 'No')], default=('1', 'No'))),
            ],
        ),
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='semesterdata',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.SessionData'),
        ),
        migrations.AddField(
            model_name='departmentdata',
            name='fid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.FacultyData'),
        ),
    ]