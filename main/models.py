from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


from django.urls import reverse

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError(" User must have an Username")

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,username,password):

        user=self.create_user(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                )

        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)



    date_joined  =models.DateTimeField(auto_now_add=True)
    last_login  =models.DateTimeField(auto_now_add=True)
    is_admin =models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    is_active =models.BooleanField(default=False)
    is_superadmin =models.BooleanField(default=False)
    is_recruiter =models.BooleanField(default=False)



    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username','first_name','last_name']

    objects=MyAccountManager()

    def __str__(self):
        return self.email


    def  has_perm(self,perm,obj=None):
        return self.is_admin


    def has_module_perms(self, add_label):
        return True

    def get_all_permissions(user):
        if user.is_superadmin:
            return set()


class UserProfile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    address_line_1 = models.CharField(blank=True, max_length=50)
    address_line_2 = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=50)
    state = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    pin_code =models.IntegerField(null=True,blank=True)
    highest_qualification=models.IntegerField(null=True,blank=True)
    year_of_passout=models.IntegerField(null=True,blank=True)
    degree_college=models.CharField(blank=True, max_length=50)
    cgpa=models.IntegerField(null=True,blank=True)
    degree_passout=models.IntegerField(null=True,blank=True)
    plus_two_school=models.CharField(blank=True, max_length=50)
    plus_two_persentage=models.IntegerField(null=True,blank=True)
    plus_two_passout=models.IntegerField(null=True,blank=True)
    tenth_school=models.CharField(blank=True, max_length=50)
    tenth_year=models.IntegerField(null=True,blank=True)
    tenth_persentage=models.IntegerField(null=True,blank=True)
    currentRole=models.CharField(blank=True, max_length=50)
    currentCTC=models.IntegerField(null=True,blank=True)
    ECTC=models.IntegerField(null=True,blank=True)
    # skills=models.ManyToManyField()
    total_experiance=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    NoticePeriod=models.CharField(blank=True, max_length=50)#date
    CurrentLocation=models.CharField(blank=True, max_length=50)
    PreferredLocations=models.CharField(blank=True, max_length=50)#array

    # def __str__(self):
    #     return self.user.user

    def full_address(self):
        return f'{self.address_line_1}{self.address_line_2}'



class RecruiterProfile(models.Model):
    user = models.ForeignKey("Account",on_delete=models.CASCADE)
    company_name=models.CharField(max_length=500)
    designation=models.CharField(max_length=200)
    company_mail=models.EmailField()
    documents=models.FileField(null=True)
    company_GST=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    is_approved=models.BooleanField(default=False)
    is_pending=models.BooleanField(default=True)
    is_rejected=models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


# class userResume(models.Model):
#     user = models.ForeignKey("Account",related_name='userresume',on_delete=models.CASCADE)
#     resume=models.FileField(null=True)

