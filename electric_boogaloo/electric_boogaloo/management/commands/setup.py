from django.core.management import call_command
from django.core.management.base import BaseCommand
import pip


class Command(BaseCommand):
    help = 'Runs basic setup commands'

    def handle(self, *args, **options):
        # pip.main(['install', '-r', ''])  # todo: pip install from this command
        call_command('migrate', {'interactive': False})