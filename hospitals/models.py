import uuid

from django.db import models

from vets.models import Vet


class Hospital(models.Model):
    chief_vet = models.ForeignKey(Vet, models.SET_NULL, blank=True, null=True)
    name = models.CharField('Name', max_length=255)
    address = models.CharField('Address', max_length=255)
    location = models.CharField('Location', max_length=255)
    license = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
