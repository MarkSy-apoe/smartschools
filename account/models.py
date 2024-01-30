from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
STATE = (
	("lagos", "Lagos"),
	("abuja", "Abuja"),
)

ACC_TYPE =(
	("ministerOE", "Minister of education"),
	("commissioner", "Commissioners"),
	("officestaff", "Office Staff"),
	("fedraldistrict", "Fedral Head of District"),
	("statedistrict", "State Head of District"),
	("principal", "Principal"),
	("teacher", "Teacher"),
	("student", "Student"),
	("schooladmin", "School Admin"),
)

SCHOOL_GOV = (
    ("fedral", "Fedral"),
    ("state", "State"),
	("private", "Private"),
)

SCHOOL_LVL = (
    ("primary", "Primary School"),
    ("secondary", "Secondary School"),
	("juniorsecondary", "Junior Secondary School"),
	("seniorsecondary", "Senior Secondary School"),
	("poly", "Polytechnic"),
	("uni", "University"),
)

DISTRICTFED = (
	("nw", "North West"),
	("ne", "North East"),
	("nc", "North Central"),
	("ss", "South South"),
	("se", "South East"),
	("sw", "South West"),
)

class MyAccountManager(BaseUserManager):

	def create_user(self, email, username, first_name, last_name, password=None):
		if not email:
			raise ValueError("Users must have an email address.")
		if not username:
			raise ValueError("Users must have an username.")
		if not first_name:
			raise ValueError("Users must have an first_name.")
		if not last_name:
			raise ValueError("Users must have an last_name.")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			first_name=first_name,
			last_name=last_name,
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, last_name, password):
		user = self.create_user(
			email=email,
			username=username,
			first_name=first_name,
			last_name=last_name,
			password=password,
		)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.is_confirmed = True

		user.save(using=self._db)
		return user
	

class Account(AbstractBaseUser):
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name 		= models.CharField(max_length=30, null=True)
	last_name 		= models.CharField(max_length=30, null=True)
	username 		= models.CharField(max_length=30, unique=True)
	date_joined 	= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	last_login 		= models.DateTimeField(verbose_name="last_login", auto_now=True)
	is_admin 		= models.BooleanField(default=False)
	is_active 		= models.BooleanField(default=True)
	is_staff 		= models.BooleanField(default=False)
	is_superuser 	= models.BooleanField(default=False)	
	is_confirmed		= models.BooleanField(default=False)
	is_approved = models.BooleanField(default=False)
	accounttype = models.CharField(max_length=30, choices=ACC_TYPE)

	objects = MyAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
	
	
class School(models.Model):
	schoolcrest = models.ImageField(upload_to='schoolcrest/', null=True)
	name        = models.CharField(max_length=70, unique=True)
	vision      = models.TextField()
	mission     = models.TextField()
	is_approved = models.BooleanField(default=False)
	is_waecaccredited = models.BooleanField(default=False)
	is_suspended = models.BooleanField(default=False)
	has_principal = models.BooleanField(default=False)
	joined		= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	state       = models.CharField(max_length=30, choices=STATE, null = True)
	schoolLvl   = models.CharField(max_length=30, choices=SCHOOL_LVL)
	schoolGov   = models.CharField(max_length=30, choices=SCHOOL_GOV)
	slug		= models.SlugField(null=True, unique=True)
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse("schoolprofile", kwargs={"pk": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)
	
class PrincipalProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	dp = models.ImageField(upload_to='profileimages/', null=True)
	school   = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username

class StudentProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	dp = models.ImageField(upload_to='profileimages/', null=True)
	school = models.ForeignKey(School, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username
	
class TeacherProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
	dp = models.ImageField(upload_to='profileimages/', null=True)
	school = models.ForeignKey(School, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username
	
class MinisterProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	
	def __str__(self):
		return "@" + self.user.username

class CommissionerProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	state   = models.CharField(max_length=30, choices=STATE, null =True)
	
	def __str__(self):
		return "@" + self.user.username
	
class FedralDistrictHeadProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	district = models.CharField(max_length=30, choices=DISTRICTFED)
	
	def __str__(self):
		return "@" + self.user.username
	
class StateDistrictHeadProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	
	def __str__(self):
		return "@" + self.user.username
	
class Ministeroffice(models.Model):
	officeadmin = models.OneToOneField(MinisterProfile, on_delete=models.SET_NULL, null=True)
	
class Commisioneroffice(models.Model):
	officeadmin = models.OneToOneField(CommissionerProfile, on_delete=models.SET_NULL, null=True)
	
class FedralDistrictoffice(models.Model):
	officeadmin = models.OneToOneField(FedralDistrictHeadProfile, on_delete=models.SET_NULL, null=True)
	
class StateDistrictoffice(models.Model):
	officeadmin = models.OneToOneField(StateDistrictHeadProfile, on_delete=models.SET_NULL, null=True)
	
class OfficeofMinisterstaffProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	office = models.ForeignKey(Ministeroffice, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username
	
class OfficeofCommisionerstaffProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	office = models.ForeignKey(Commisioneroffice, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username
	
class OfficeofFedDistrictstaffProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	office = models.ForeignKey(FedralDistrictoffice, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username
	
class OfficeofStateDistrictstaffProfile(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	dp = models.ImageField(upload_to='officeprofileimages/', null=True)
	office = models.ForeignKey(StateDistrictoffice, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return "@" + self.user.username


class Post(models.Model):
	user    = models.OneToOneField(Account, on_delete=models.CASCADE)
	content = models.TextField()

	
	