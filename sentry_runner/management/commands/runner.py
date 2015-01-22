from __future__ import print_function

from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Run arbitrary script within Sentry environment'

    option_list = BaseCommand.option_list + (
        make_option('--file', dest='file', help='Path to Python script'),
    )

    def handle(self, **options):
        file = options['file']
        if file is None:
            raise CommandError('--file option is required')
        execfile(options['file'])
