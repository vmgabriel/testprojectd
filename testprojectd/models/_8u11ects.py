"""Content _8u11ects"""

# Libraries
from django.db import models

 # Modules
from . import students


class _8u11ects(models.Model):
    _63t8 = models.CharField("_63t8", null=True, blank=True, max_length=120, )
    s5bm6m1d5tv = models.CharField("s5bm6m1d5tv", null=True, blank=True, max_length=120, )
    wt = models.CharField("wt", null=True, blank=True, max_length=120, )
    students_sc = models.ForeignKey(students.Students, on_delete=models.CASCADE)

    def __str__(self):
        return f"_8u11ects {self.pk}"

    def __repr__(self):
        return str(self)