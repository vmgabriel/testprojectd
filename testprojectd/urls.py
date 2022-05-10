"""All Urls of Testprojectd"""

# Libraries
from django.urls import path

# Views
from . import views


app_name = "testprojectds"
urlpatterns = [
    # StUdeNtS
    path(
        "studentss/",
        views.ListStudentsView.as_view(),
        name="studentss",
    ),
    path(
        "studentss/new/",
        views.StudentsCreateView.as_view(),
        name="students-new",
    ),
    path(
        "studentss/<int:pk>/edit/",
        views.StudentsUpdateView.as_view(),
        name="students-edit",
    ),
    path(
        "studentss/<int:pk>/delete/",
        views.delete_students_view,
        name="students-delete",
    ),

    # _8U11eCtS
    path(
        "_8u11ectss/",
        views.List_8u11ectsView.as_view(),
        name="_8u11ectss",
    ),
    path(
        "_8u11ectss/new/",
        views._8u11ectsCreateView.as_view(),
        name="_8u11ects-new",
    ),
    path(
        "_8u11ectss/<int:pk>/edit/",
        views._8u11ectsUpdateView.as_view(),
        name="_8u11ects-edit",
    ),
    path(
        "_8u11ectss/<int:pk>/delete/",
        views.delete__8u11ects_view,
        name="_8u11ects-delete",
    ),

]