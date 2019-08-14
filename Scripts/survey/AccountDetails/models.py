from django.db import models
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager)
from django.core.exceptions import ValidationError
def validate_rating(value):
    if value<1 or value>5 :  # Your conditions here
        raise ValidationError('%s is an Invalid Rating' % value)
class Workers(models.Model):
	name = models.CharField(max_length=255,blank=False,null=False)
	city = models.CharField(max_length=255,blank=False,null=False)
	district = models.CharField(max_length=255,blank=False,null=False)
	state = models.CharField(max_length=255,blank=False,null=False)
	people_contacted = models.IntegerField(default=0)
	reviews_collected = models.IntegerField(default=0)
	education_rating = models.IntegerField(validators=[validate_rating],blank=False,null=False)
	health_rating = models.IntegerField(validators=[validate_rating],blank=False,null=False)
	electricity_rating = models.IntegerField(validators=[validate_rating],blank=False,null=False)
	transport_rating = models.IntegerField(validators=[validate_rating],blank=False,null=False)
	employment_rating = models.IntegerField(validators=[validate_rating],blank=False,null=False)
def validate_number(value):
    if value<1 or value>4 :  # Your conditions here
        raise ValidationError('%s is an Invalid Level' % value)
class UserManager(BaseUserManager):
	def create_user(self,email,level,contact,full_name,city,district,state,password=None,is_active=True,is_staff=False,is_admin=False):
		if not email:
			raise ValueError("User must have an email address")
		if not level:
			raise ValueError("User must have a Level of leadership")
		if not password:
			raise ValueError("Users must have a password")
		if not full_name:
			raise ValueError("User must have a Full name")
		if not contact:
			raise ValueError("User must have a contact Number")
		if not city:
			raise ValueError("User must enter City")
		if not district:
			raise ValueError("User must enter district")
		if not state:
			raise ValueError("User must enter state")
        
		user_obj = self.model(
			email=self.normalize_email(email),
			level=level,
			contact=contact,
			full_name=full_name,
			city=city,
			district=district,
			state=state,
			)
		user_obj.set_password(password)#change user password
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active= is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self,email,contact,full_name,level,city,district,state,password=None):
		user = self.create_user(email,level,contact,full_name,city,district,state,password=password,is_staff=True)

		return user

	def create_superuser(self,email,contact,full_name,level,city,district,state,password=None):
		user = self.create_user(email,level,contact,full_name,city,district,state,password=password,is_active=True,is_staff=True,is_admin=True)

		return user	
    
class User(AbstractBaseUser):
	email    	=models.EmailField(max_length=255,unique=True)
	full_name	=models.CharField(max_length=255,blank=True,null=True)
	city		=models.CharField(max_length=255,blank=True,null=True)
	state 		=models.CharField(max_length=255,blank=True,null=True)
	district 	=models.CharField(max_length=255,blank=True,null=True)
	contact 	=models.IntegerField(blank=True,null=True)
	active		=models.BooleanField(default=True)
	staff  		=models.BooleanField(default=False)
	admin   	=models.BooleanField(default=False)
	#confirm	=models.BooleanField(default=False)
	#confirmed_date	=models.DateTimeField(default=False)
	level 		=models.IntegerField(validators=[validate_number],blank=False,null=False)
	USERNAME_FIELD = 'email'#username
	REQUIRED_FIELDS = ['level','full_name','contact','city','state','district']

	objects=UserManager()

	def __str__(self):
		return self.email
	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.staff

	def has_perm(self,perm,obj=None):
		return True

	def has_module_perms(self,app_label):
		return True
	@property
	def is_staff(self):
		return self.staff
	
	@property
	def is_admin(self):
		return self.admin
	
	@property
	def is_active(self):
		return self.active
	

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)