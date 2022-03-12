from django.db import models as _m
from django.utils.translation import gettext_lazy as _


class Semester(_m.IntegerChoices):
    FIRST = 1, _("1-st")
    SECOND = 2, _("2-nd")
    THIRD = 3, _("3-rd")
    FORTH = 4, _("4-th")
    FIFTH = 5, _('5-th')
    SIXTH = 6, _('6-th')
    SEVENTH = 7, _('7-th')
    EIGHTH = 8, _('8-th')
    NINTH = 9, _('9-th')
    TENTH = 10, _("10-th")


class Degree(_m.TextChoices):
    BACHELORS = "BS", _("Bachelor's Degree")
    MASTERS = "MS", _("Master's Degree")
    PHD = "PHD", _("PhD")
    DIPLOMA = "DPL", _("Diploma")
