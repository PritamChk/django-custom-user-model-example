from enum import Enum as _enum


class Semester(_enum):
    FIRST = "1-st"
    SECOND = "2-nd"
    THIRD = "3-rd"
    FORTH = "4-th"
    FIFTH = '5-th'
    SIXTH = '6-th'
    SEVENTH = '7-th'
    EIGHTH = '8-th'
    NINTH = '9-th'
    TENTH = "10-th"

    @classmethod
    def choices(cls):
        return ((tag.value, tag.name) for tag in cls)


class Degree(_enum):
    BACHELORS = "Bachelor's Degree"
    MASTERS = "Master's Degree"
    PHD = "PhD"
    DIPLOMA = "Diploma"

    @classmethod
    def choices(cls):
        return ((tag.value, tag.name) for tag in cls)
