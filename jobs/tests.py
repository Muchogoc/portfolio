from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.apps import apps
from jobs.models import Job
from .apps import JobsConfig
from .views import homepage as f_view
from .views import detail as s_view


class JobTest(TestCase):

    def create_job(self, image="sth.png", summary="good job"):
        return Job.objects.create(image=image, summary=summary)

    # models test
    def test_whatever_creation(self):
        m = self.create_job()
        self.assertTrue(isinstance(m, Job))
        self.assertEqual(m.__str__(), m.summary)

    # views test
    def test_homepage_view(self):
        m = self.create_job()
        url = reverse(f_view)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(str.encode(m.summary), resp.content)

    def test_details_view(self):

        self.factory = RequestFactory()
        self.job = self.create_job()

        request = self.factory.get('jobs/<int:job_id>')
        request.job = self.job
        response = s_view(request, job_id=1)
        self.assertEqual(response.status_code, 200)


class JobsConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(JobsConfig.name, 'jobs')
        self.assertEqual(apps.get_app_config('jobs').name, 'jobs')
