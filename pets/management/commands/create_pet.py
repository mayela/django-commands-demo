from django.core.management.base import BaseCommand, CommandError

from pets.models import Animal


class Command(BaseCommand):
    help = "Create a new pet from the cli"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Pet's name")
        parser.add_argument('breed', type=str, help="Pet's breed")
        parser.add_argument('age', type=int, help="Pet's age")
        parser.add_argument('sound', type=str, help="Pet's sound")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        breed = kwargs['breed']
        age = kwargs['age']
        sound = kwargs['sound']
        
        try:
            Animal.objects.create(name=name, breed=breed, age=age, sound=sound)
        except:
            raise CommandError("New pet can not be created")
