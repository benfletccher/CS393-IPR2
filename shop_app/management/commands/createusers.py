from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from shop_app.models import Vendor, Customer, Cadet

class Command(BaseCommand):
    def handle(self, **options):
        groups = ['Vendor', 'Customer']
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)