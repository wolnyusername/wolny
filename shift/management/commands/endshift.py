from django.core.management.base import BaseCommand
from shift.models import Shift
import datetime


class Command(BaseCommand):
    help = 'ends shifts that had not been ended'

    def handle(self, *args, **options):
        for i in Shift.objects.filter(end_time=None):
            max_shift = datetime.timedelta(minutes=2)
            if datetime.datetime.now(datetime.timezone.utc) - Shift.objects.get(id=i.id).start_time >= max_shift:
                Shift.objects.filter(id=i.id).update(end_time=(Shift.objects.get(id=i.id).start_time+max_shift))
