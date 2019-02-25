from django.shortcuts import resolve_url
from django.test import TestCase
from node_manager.models import Node
from io import BytesIO
from django.core import mail
from django.contrib.auth.models import User


class TestUpload(TestCase):

    # tests must subclass djangos test case
    def testNodePing(self):
        # tests must start with test
        node = Node.objects.create(name="Test node")
        self.assertEqual(node.last_contact, None)
        # we make new things to test which get destroyed at the end
        response = self.client.post(resolve_url("upload", node.id))
        # this makes a fake request to the website, we reverse engin the URL
        # using resolve_url
        self.assertEqual(response.status_code, 200)
        # checks the httpresponse of the fake request
        self.assertEqual(response.content, b"")
        # sees if the httpresponse is an empty binary string
        node.refresh_from_db()
        # we need to update the local node object since we changed last_contact
        self.assertNotEqual(node.last_contact, None)

    def testNodeImageUpload(self):
        node = Node.objects.create(name="Test node")
        self.assertEqual(node.photo_set.count(), 0)
        image = BytesIO(b'catcatcat')
        image.name = 'image.jpg'
        response = self.client.post(resolve_url("upload", node.id), {'image': image})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(node.photo_set.count(), 1)

        # We've established that there is one photo.
        # Load the photo, and make sure that the image has the correct content.
        photo = node.photo_set.order_by("-pub_date").first()  # TODO: Replace None with the first (and only) node photo.
        self.assertEqual(photo.photo.read(), b'catcatcat')

    def testNode405(self):
        node = Node.objects.create(name="Test node")
        response = self.client.get(resolve_url("upload", node.id))
        self.assertEqual(response.status_code, 405)

    def testEmail(self):
        node = Node.objects.create(name="Test node")
        test_user = User()
        test_user.username = "test"
        test_user.password = "foo"
        test_user.email = "jenny.thorne3006@gmail.com"
        test_user.save()
        node.contacts.add(test_user)
        image = BytesIO(b'catcatcat')
        image.name = 'image.jpg'
        self.client.post(resolve_url("upload", node.id), {'image': image})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].attachments[0][1], b'catcatcat')

    def testBooButton(self):
        node = Node.objects.create(name="Test node")
        self.assertEqual(node.email_users, True)
        node.email_users = False
        node.save()
        self.assertEqual(node.email_users, False)
