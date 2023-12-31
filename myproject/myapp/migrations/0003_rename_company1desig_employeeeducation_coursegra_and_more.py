# Generated by Django 4.2.7 on 2023-11-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_employeedetail_user_employeeexperience_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='company1desig',
            new_name='coursegra',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='company1duration',
            new_name='coursehsc',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='company1name',
            new_name='coursepg',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='company1salary',
            new_name='coursessc',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='coursegra',
            new_name='company1desig',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='coursehsc',
            new_name='company1duration',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='coursepg',
            new_name='company1name',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='coursessc',
            new_name='company1salary',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company2desig',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company2duration',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company2name',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company2salary',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company3desig',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company3duration',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company3name',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company3salary',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='percentagegra',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='percentagehsc',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='percentagepg',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='percentagessc',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='schoolclggra',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='schoolclghsc',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='schoolclgpg',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='schoolclgssc',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='yearofpassinggra',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='yearofpassinghsc',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='yearofpassingpg',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='yearofpassingssc',
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='percentagegra',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='percentagehsc',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='percentagepg',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='percentagessc',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='schoolclggra',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='schoolclghsc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='schoolclgpg',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='schoolclgssc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yearofpassinggra',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yearofpassinghsc',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yearofpassingpg',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yearofpassingssc',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company2desig',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company2duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company2name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company2salary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company3desig',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company3duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company3name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='company3salary',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
