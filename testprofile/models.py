from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import Semester as _sem, Degree as _deglevel

User = get_user_model()


class Department(models.Model):
    name = models.CharField("Department Name", max_length=350, db_index=True)
    domain = models.CharField(
        "Domain Name",
        max_length=300,
        help_text="e.g., Domain : Computer Science"
    )
    degree = models.CharField(
        "Degree Level",
        max_length=100,
        blank=True,
        choices=_deglevel.choices(),
        default=_deglevel.BACHELORS
    )
    #students = ...


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        primary_key=True,
        related_name="student_profile"
    )
    university_roll = models.PositiveSmallIntegerField(
        _("University Roll"),
        unique=True, db_index=True, help_text="Your University Roll No - (e.g. - 13071020030)"
    )
    current_sem = models.CharField(
        _("Choose Sem [1-10]-th"),
        choices=_sem.choices(),
        default=_sem.FIRST,
        max_length=10,
        db_index=True,
        help_text="Select Your On Going Sem🔢",
    )
    depertment = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name="students"
    )

    def __str__(self) -> str:
        return f"{self.university_roll}"
