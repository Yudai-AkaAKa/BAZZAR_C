from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
""" ユーザー種別ごとのパターン"""
class UserType(models.Model):
    """ ユーザ種別 """
    typename = models.CharField(verbose_name='ユーザ種別',
                                max_length=150)

    def __str__(self):
        return f'{self.id} - {self.typename}'

USERTYPE_COMP = 100
USERTYPE_USER = 200
USERTYPE_DEFAULT = USERTYPE_USER

class CustomUserManager(UserManager):
    """ 拡張ユーザーモデル向けのマネージャー """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """ 拡張ユーザーモデル """

    class Meta(object):
        db_table = 'custom_user'

    #作成したマネージャークラスを使用
    objects = CustomUserManager()

    # モデル内にユーザ種別を持つ
    userType = models.ForeignKey(UserType,
                                verbose_name='ユーザ種別',
                                null=True,
                                blank=True,
                                on_delete=models.PROTECT)
    def __str__(self):
        return self.username

class UserDetailSupplier(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_supplier',
                                on_delete=models.CASCADE)
    # COMPユーザ向けの項目
    companyName = models.CharField(
                                   max_length=100,
                                   null=True,
                                   blank=True,
                                )
    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id} - {self.companyName}'

class UserDetailBuyer(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_buyer',
                                on_delete=models.CASCADE)
    # USERユーザ向けの項目
    nearestStation = models.CharField(
                                   max_length=100,
                                   null=True,
                                   blank=True,
                                )
    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id} - {self.nearestStation}'



""" 一応成功したやつ
class CustomUser(AbstractUser,PermissionsMixin):
    #ユーザーと事業者共通で必要
    userid = models.AutoField(verbose_name='userid',primary_key=True)
    username = models.CharField(verbose_name='name', max_length=20,unique=True)
    #Trueが一般ユーザー,Falseが事業者
    usertype = models.BooleanField(verbose_name='usertype',blank=True, null=True,default=True)
    password = models.CharField(verbose_name='password', max_length=128)
    mail=models.EmailField(verbose_name='メールアドレス',max_length=40)
    phone=models.CharField(verbose_name='電話番号',max_length=11,blank=True, null=True)
    #事業者のみで必要
    age=models.IntegerField(verbose_name='年齢',blank=True, null=True)
    adress=models.CharField(verbose_name='住所',max_length=80,blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='lastlogin', blank=True, null=True)

    class Meta():
        verbose_name_plural = 'CustomUser'
"""

