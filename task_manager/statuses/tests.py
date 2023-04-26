from django.test import TestCase
from task_manager.statuses.models import Status
from django.core.exceptions import ObjectDoesNotExist


class StatusTest(TestCase):

    def setUp(self):
        self.status = Status()
        self.status.name = 'Test'
        self.status.save()

    def tearDown(self):
        self.status.delete()

    def test_update_status(self):
        self.status.name = 'NewName'
        self.status.save()
        self.assertEqual(self.status.name, 'NewName')

    def test_delete_status(self):
        status = Status.objects.get(pk=1)
        status.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=1)
