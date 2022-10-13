from django.core.management.base import BaseCommand

from shift.models import Shift


class Command(BaseCommand):
    help = 'ends shifts that had not been ended'

    def handle(self, *args, **options):
        for i in Shift.objects.filter(end_time=None):
            max_shift = datetime.timedelta(minutes=2)
            if (datetime.datetime.now(datetime.timezone.utc) - i.start_shift) >= max_shift:
                i.update(end_time=(i.start_shift+max_shift))
