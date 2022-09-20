from django.core.management.base import BaseCommand
from shift.models import Shift
import datetime


class Command(BaseCommand):
    help = 'ends shifts that had not been ended'

    def handle(self, *args, **options):
        for i in Shift.objects.filter(end_time=None):
            z=Shift.objects.get(id=i.id)
            delta = datetime.timedelta(hours=1)
            now = datetime.datetime.now(datetime.timezone.utc)
            if now - z.start_time >= delta:
                Shift.objects.filter(id=i.id).update(end_time=z.start_time+delta)
                print(z)
