# Generated by Django 4.2.4 on 2024-01-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('accounttype', models.CharField(choices=[('ministerOE', 'Minister of education'), ('commissioner', 'Commissioners'), ('officestaff', 'Office Staff'), ('fedraldistrict', 'Fedral Head of District'), ('statedistrict', 'State Head of District'), ('principal', 'Principal'), ('teacher', 'Teacher'), ('student', 'Student'), ('schooladmin', 'School Admin')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commisioneroffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FedralDistrictHeadProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('district', models.CharField(choices=[('nw', 'North West'), ('ne', 'North East'), ('nc', 'North Central'), ('ss', 'South South'), ('se', 'South East'), ('sw', 'South West')], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='FedralDistrictoffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeadmin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.fedraldistrictheadprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Ministeroffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PrincipalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='profileimages/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolcrest', models.ImageField(null=True, upload_to='schoolcrest/')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('is_waecaccredited', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('schoolLvl', models.CharField(choices=[('primary', 'Primary School'), ('secondary', 'Secondary School'), ('juniorsecondary', 'Junior Secondary School'), ('seniorsecondary', 'Senior Secondary School'), ('poly', 'Polytechnic'), ('uni', 'University')], max_length=30)),
                ('schoolGov', models.CharField(choices=[('fedral', 'Fedral'), ('state', 'State'), ('private', 'Private')], max_length=30)),
                ('principal', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.principalprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StateDistrictHeadProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='profileimages/')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='profileimages/')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='StateDistrictoffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeadmin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.statedistrictheadprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeofStateDistrictstaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.statedistrictoffice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeofMinisterstaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ministeroffice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeofFedDistrictstaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.fedraldistrictoffice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeofCommisionerstaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.commisioneroffice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='MinisterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.AddField(
            model_name='ministeroffice',
            name='officeadmin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ministerprofile'),
        ),
        migrations.CreateModel(
            name='CommissionerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(null=True, upload_to='officeprofileimages/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.AddField(
            model_name='commisioneroffice',
            name='officeadmin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.commissionerprofile'),
        ),
    ]
