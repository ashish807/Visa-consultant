from django.contrib import sitemaps
from django.urls import reverse

class staticviewsSitemap(sitemaps.sitemap):

    priority = 0.5
    changefreq = "weekly"

    def items(self):

        return [

            'visaPage:home',
            'visaPage:about',
            'visaPage:conatct',
            'visapage:blog',
            'visapage:media',


        ]

def location(self, item):
    return reverse(item)

