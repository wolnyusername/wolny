import datetime

from django.core.management.base import BaseCommand
from shift.models import Shift


class Command(BaseCommand):
    help = 'ends shifts that had not been ended'

    def handle(self, *args, **options):
        for i in Shift.objects.filter(end_time=None):
            max_shift = datetime.timedelta(minutes=2)
            start_shift = Shift.objects.get(id=i.id).start_time
            if (datetime.datetime.now(datetime.timezone.utc) - start_shift) >= max_shift:
                Shift.objects.filter(id=i.id).update(end_time=(start_shift+max_shift))
