from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Setup default user groups and permissions"

    def handle(self, *args, **kwargs):
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_create", "can_edit"],
            "Admins": ["can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                permission = Permission.objects.get(codename=perm_codename)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully!"))

