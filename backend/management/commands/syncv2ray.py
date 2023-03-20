from django.core.management.base import BaseCommand, CommandError
from sspanel.models import Account
from backend.tasks import v2ray_add_user

class Command(BaseCommand):

    help = 'Synchronize users to v2ray'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f'start synchronize users to v2ray...'))
        for account in Account.objects.filter(enable=True).select_related('user'):
            v2ray_add_user.delay(str(account.uuid))
            self.stdout.write(self.style.SUCCESS(f'add account to v2ray: {account.username}'))