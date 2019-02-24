from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Node, Photo
from django.core.mail import EmailMessage


def index(request):
    return HttpResponse()


def email(node, file_list):
    recipients = []
    for user in node.contacts.all():
        if user.is_active:
            recipients.append(user.email)

    email = EmailMessage(
        'Cat detected',
        'Motion detected on {}'.format(node.name),
        'jenny@jennythorne.co.uk',
        recipients,
    )

    for pic in file_list:
        email.attach_file(pic)
    email.send(fail_silently=False)


def upload(request, node_pk):
    if request.method == 'POST':
        node = get_object_or_404(Node, pk=node_pk)
        node.last_contact = timezone.now()
        node.save()
        # we make changes then update database, otherwise EVERYTHING IS GOONNEE
        file_list = []
        if request.FILES.getlist("image"):
            for image in request.FILES.getlist("image"):
                # there are GET requests and POST requests
                # django sorts everything into 2 piles,
                # one for files and one for body
                # its a weird dict, you can have non unique keys
                # so you want FILES.getlist incase you have multiple
                # of the same name
                new_photo = Photo(node=node, photo=image)
                new_photo.save()
                file_list.append(new_photo.photo.path)
            email(node, file_list)
        return HttpResponse()
    else:
        return HttpResponse(status=405)
