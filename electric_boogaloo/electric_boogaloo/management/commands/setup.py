from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Runs basic setup commands'
    commands = (
        ('create_development_users', {}),)

    def handle(self, *args, **options):
        for command, kwargs in self.commands:
            call_command(command, **kwargs)