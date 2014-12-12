from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Runs basic setup commands'

    def handle(self, *args, **options):
        pass