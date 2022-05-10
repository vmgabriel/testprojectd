"""Views of Testprojectd"""

# Libraries
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Core
from core.views import FilteredListView

# App Contents
from . import models, filters, forms


# Students

class ListStudentsView(LoginRequiredMixin, FilteredListView):
    template_name = "students/list.html"
    filterset_class = filters.StudentsFilter
    model = models.students.Students
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class StudentsCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Students"""
    form_class = forms.StudentsForm
    success_url = reverse_lazy("testprojectds:studentss")
    template_name = "students/new.html"


class StudentsUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Students"""
    form_class = forms.StudentsForm
    success_url = reverse_lazy("testprojectds:studentss")
    template_name = "students/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.students.Students, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_students_view(request, pk):
    students = get_object_or_404(models.students.Students, pk=pk)
    students.delete()
    return redirect("testprojectds:studentss")


# _8u11ects

class List_8u11ectsView(LoginRequiredMixin, FilteredListView):
    template_name = "_8u11ects/list.html"
    filterset_class = filters._8u11ectsFilter
    model = models._8u11ects._8u11ects
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class _8u11ectsCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View _8u11ects"""
    form_class = forms._8u11ectsForm
    success_url = reverse_lazy("testprojectds:_8u11ectss")
    template_name = "_8u11ects/new.html"


class _8u11ectsUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View _8u11ects"""
    form_class = forms._8u11ectsForm
    success_url = reverse_lazy("testprojectds:_8u11ectss")
    template_name = "_8u11ects/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models._8u11ects._8u11ects, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete__8u11ects_view(request, pk):
    _8u11ects = get_object_or_404(models._8u11ects._8u11ects, pk=pk)
    _8u11ects.delete()
    return redirect("testprojectds:_8u11ectss")


