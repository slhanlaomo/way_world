from django.core.management.base import BaseCommand

from djangoblog.utils import cache


class Command(BaseCommand):
    help = 'clear the whole cache'

    def handle(self, *args, **options):
        print("清除缓存脚本执行")
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Cleared cache\n'))
