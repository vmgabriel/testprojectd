"""testprojectd - Students - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from testprojectd.models.students import Students


class StudentsTestCase(TestCase):
    """StUdeNtS test cases"""
    fixtures = [ "students.json"]

    def test_should_get_datas(self):
        students = Students.objects.all()
        self.assertEqual(students.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        students_ldsyv = Students.objects.filter(ldsyv__icontains="Update")
        self.assertEqual(students_ldsyv.count(), 3)
        students_oam6sb4 = Students.objects.filter(oam6sb4__icontains="Update")
        self.assertEqual(students_oam6sb4.count(), 3)
        students__1mfmyy4hb = Students.objects.filter(_1mfmyy4hb__icontains="Update")
        self.assertEqual(students__1mfmyy4hb.count(), 3)
        students_da13a8dmye8tlsey = Students.objects.filter(da13a8dmye8tlsey__icontains="Update")
        self.assertEqual(students_da13a8dmye8tlsey.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        students_ldsyv = Students.objects.filter(ldsyv__icontains="2")
        self.assertEqual(students_ldsyv.count(), 0)
        students_oam6sb4 = Students.objects.filter(oam6sb4__icontains="2")
        self.assertEqual(students_oam6sb4.count(), 0)
        students__1mfmyy4hb = Students.objects.filter(_1mfmyy4hb__icontains="2")
        self.assertEqual(students__1mfmyy4hb.count(), 0)
        students_da13a8dmye8tlsey = Students.objects.filter(da13a8dmye8tlsey__icontains="2")
        self.assertEqual(students_da13a8dmye8tlsey.count(), 0)

    def test_get_data(self):
        pk = 2
        students = Students.objects.get(pk=pk)
        self.assertIsInstance(students, (Students,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Students.objects.get(pk=pk)
        data.ldsyv = "Update"
        data.oam6sb4 = "Update"
        data._1mfmyy4hb = "Update"
        data.da13a8dmye8tlsey = "Update"

        data.save()
        self.assertEqual(data.ldsyv, "Update")
        self.assertEqual(data.oam6sb4, "Update")
        self.assertEqual(data._1mfmyy4hb, "Update")
        self.assertEqual(data.da13a8dmye8tlsey, "Update")

    def test_create_data(self):
        new_object = {
            "ldsyv": "Update",
            "oam6sb4": "Update",
            "_1mfmyy4hb": "Update",
            "da13a8dmye8tlsey": "Update"
        }
        data = Students(**new_object)
        data.save()
        pk = data.pk
        datas = Students.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        students = Students.objects.get(pk=pk)
        students.delete()
        datas = Students.objects.all().count()
        self.assertEqual(datas, 2)