from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

PASSWORD = 'test1234'


class Command(BaseCommand):
    help = 'Create users required for development'
    users = (
        {
            'username': 'admin',
            'email': 'admin@electric-boogaloo.local',
            'password': PASSWORD,
            'is_staff': True,
            'is_active': True,
            'is_superuser': True,
        },
    )

    def handle(self, *args, **options):
        for user in self.users:
            self.create_user(user)

    def create_user(self, obj):
        user, created = User.objects.get_or_create(**obj)