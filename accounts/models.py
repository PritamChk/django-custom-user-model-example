from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from uuid import uuid4


class BaseAccountManager(BaseUserManager):
    def create_user(self, first_name:str, last_name:str, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not first_name:
            raise ValueError(_('The First Name must be set'))
        if not last_name:
            raise ValueError(_('The Last Name must be set'))
        if not first_name:
            raise ValueError(_('The First Name must be set'))
        if not last_name:
            raise ValueError(_('The Last Name must be set'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name.title(),
            last_name=last_name.title(),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(first_name,last_name,email, password, **extra_fields)


class BaseAccount(AbstractUser,PermissionsMixin):
    username = None
    id = models.UUIDField(primary_key=True, editable=False,
                          auto_created=True, default=uuid4)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(
        verbose_name="Email Id",
        unique=True, max_length=350,
        help_text="This will be used as username for login"
    )

    is_superuser = models.BooleanField(
        _("admin status"),
        default=False,
        help_text=_(
            "Designates whether the user can edit everything into this admin site."),
    )
    
    objects = BaseAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    class Meta:
        ordering = ['first_name','last_name']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        