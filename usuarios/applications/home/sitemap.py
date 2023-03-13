from datetime import timedelta, datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
#
from applications.entrada.models import Entry


class EntrySitemap(Sitemap):

    changefreg = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Entry.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.created


class Sitemap(Sitemap):
    protocol = 'https'

    def __int__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreg(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)
