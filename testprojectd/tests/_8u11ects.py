"""testprojectd - _8u11ects - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from testprojectd.models._8u11ects import _8u11ects


class _8u11ectsTestCase(TestCase):
    """_8U11eCtS test cases"""
    fixtures = ["students.json", "_8u11ects.json"]

    def test_should_get_datas(self):
        _8u11ects = _8u11ects.objects.all()
        self.assertEqual(_8u11ects.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        _8u11ects__63t8 = _8u11ects.objects.filter(_63t8__icontains="Update")
        self.assertEqual(_8u11ects__63t8.count(), 3)
        _8u11ects_s5bm6m1d5tv = _8u11ects.objects.filter(s5bm6m1d5tv__icontains="Update")
        self.assertEqual(_8u11ects_s5bm6m1d5tv.count(), 3)
        _8u11ects_wt = _8u11ects.objects.filter(wt__icontains="Update")
        self.assertEqual(_8u11ects_wt.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        _8u11ects__63t8 = _8u11ects.objects.filter(_63t8__icontains="2")
        self.assertEqual(_8u11ects__63t8.count(), 0)
        _8u11ects_s5bm6m1d5tv = _8u11ects.objects.filter(s5bm6m1d5tv__icontains="2")
        self.assertEqual(_8u11ects_s5bm6m1d5tv.count(), 0)
        _8u11ects_wt = _8u11ects.objects.filter(wt__icontains="2")
        self.assertEqual(_8u11ects_wt.count(), 0)

    def test_get_data(self):
        pk = 2
        _8u11ects = _8u11ects.objects.get(pk=pk)
        self.assertIsInstance(_8u11ects, (_8u11ects,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = _8u11ects.objects.get(pk=pk)
        data._63t8 = "Update"
        data.s5bm6m1d5tv = "Update"
        data.wt = "Update"

        data.save()
        self.assertEqual(data._63t8, "Update")
        self.assertEqual(data.s5bm6m1d5tv, "Update")
        self.assertEqual(data.wt, "Update")

    def test_create_data(self):
        new_object = {
            "_63t8": "Update",
            "s5bm6m1d5tv": "Update",
            "wt": "Update",
            "students_sc_id": 1
        }
        data = _8u11ects(**new_object)
        data.save()
        pk = data.pk
        datas = _8u11ects.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        _8u11ects = _8u11ects.objects.get(pk=pk)
        _8u11ects.delete()
        datas = _8u11ects.objects.all().count()
        self.assertEqual(datas, 2)