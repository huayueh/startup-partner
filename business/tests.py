__author__ = 'Harvey'

from django.test import TestCase
from business.models import Business


class BusinessTestCase(TestCase):
    def test_business_model(self):
        title = 'title'
        industry = 'industry'
        location = 'location'
        content = 'content'
        contact_info = 'contact_info'
        b = Business(title=title, industry=industry, location=location, content=content, contact_info=contact_info)
        self.assertEqual(title, b.title)
        self.assertEqual(industry, b.industry)
        self.assertEqual(location, b.location)
        self.assertEqual(content, b.content)
        self.assertEqual(contact_info, b.contact_info)
