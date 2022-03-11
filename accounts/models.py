from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from uuid import uuid4
from .managers import *


class BaseAccount(AbstractUser, PermissionsMixin):
    username = None
    id = models.UUIDField(primary_key=True, editable=False,
                          auto_created=True, default=uuid4)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_no = models.CharField(
        _("Phone No(without country code or 0)"),
        max_length=15, unique=True,
        db_index=True,
        blank=True,
        null=True,
        help_text="""
            👌🏻E.g - 9881284481
            ❌ +91 9812300122
            ❌ 09812300122
        """,
        validators=[
            RegexValidator(r'^\d{10}$', "Phone no should contain 10 digits")
        ]
    )
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
        ordering = ['first_name', 'last_name']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
