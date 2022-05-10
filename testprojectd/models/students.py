"""Content Students"""

# Libraries
from django.db import models

 # Modules


class Students(models.Model):
    ldsyv = models.CharField("ldsyv", null=True, blank=True, max_length=120, )
    oam6sb4 = models.CharField("oam6sb4", null=True, blank=True, max_length=120, )
    _1mfmyy4hb = models.CharField("_1mfmyy4hb", null=True, blank=True, max_length=120, )
    da13a8dmye8tlsey = models.CharField("da13a8dmye8tlsey", null=True, blank=True, max_length=120, )

    def __str__(self):
        return f"Students {self.pk}"

    def __repr__(self):
        return str(self)