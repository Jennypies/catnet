from django.db import models
from django.contrib.auth.models import User


class Node(models.Model):
    name = models.CharField(max_length=200)
    last_contact = models.DateTimeField('Last contact', null=True, editable=False)
    contacts = models.ManyToManyField(User)
    email_users = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    # see MEDIA ROOT for more info

    def __str__(self):
        return f"{self.node} {self.pub_date}"
        # a format string containing its related node and pub date
