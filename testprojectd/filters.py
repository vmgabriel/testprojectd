"""Filter App Testprojectd"""

# Libraries
import django_filters

# Models
from . import models


class StudentsFilter(django_filters.FilterSet):
    ldsyv = django_filters.CharFilter(label="Ldsyv", lookup_expr="icontains")
    oam6sb4 = django_filters.CharFilter(label="Oam6sb4", lookup_expr="icontains")
    _1mfmyy4hb = django_filters.CharFilter(label="_1mfmyy4hb", lookup_expr="icontains")
    da13a8dmye8tlsey = django_filters.CharFilter(label="Da13a8dmye8tlsey", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("ldsyv", "Ldsyv"),
            ("oam6sb4", "Oam6sb4"),
            ("_1mfmyy4hb", "_1mfmyy4hb"),
            ("da13a8dmye8tlsey", "Da13a8dmye8tlsey"),
        ),
    )

    class Meta:
        model = models.students.Students
        fields = ["ldsyv", "oam6sb4", "_1mfmyy4hb", "da13a8dmye8tlsey", ]


class _8u11ectsFilter(django_filters.FilterSet):
    _63t8 = django_filters.CharFilter(label="_63t8", lookup_expr="icontains")
    s5bm6m1d5tv = django_filters.CharFilter(label="S5bm6m1d5tv", lookup_expr="icontains")
    wt = django_filters.CharFilter(label="Wt", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("_63t8", "_63t8"),
            ("s5bm6m1d5tv", "S5bm6m1d5tv"),
            ("wt", "Wt"),
            ("students_sc", "Students_sc"),
        ),
    )

    class Meta:
        model = models._8u11ects._8u11ects
        fields = ["_63t8", "s5bm6m1d5tv", "wt", "students_sc", ]


