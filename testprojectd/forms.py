"""Forms of Testprojectd APP"""

# Libraries
from django import forms

# Models
from . import models

class StudentsForm(forms.ModelForm):
    """Form to Students"""

    class Meta:
        model = models.students.Students
        fields = ["ldsyv", "oam6sb4", "_1mfmyy4hb", "da13a8dmye8tlsey", ]


class _8u11ectsForm(forms.ModelForm):
    """Form to _8u11ects"""
    students_sc = forms.ModelChoiceField(queryset=models.students.Students.objects.all())

    class Meta:
        model = models._8u11ects._8u11ects
        fields = ["_63t8", "s5bm6m1d5tv", "wt", "students_sc", ]


