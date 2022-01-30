from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from visaPage.models import SubVisa
from blog.models import Blog

class Static_Sitemap(Sitemap):

    priority = 0.80
    changefreq = 'weekly'

    def items(self):
        return ['visa','about','blog','login','register']

    def location(self, item):
        return reverse(item)

class Static_Sitemap2(Sitemap):

    priority = 0.64
    changefreq = 'weekly'

    def items(self):
        return SubVisa.objects.all().order_by('id')
    
    def location(self, item):
        return reverse('subvisa', args=[item.visa.slug])

class Static_Sitemap3(Sitemap):

    priority = 0.64
    changefreq = 'weekly'

    def items(self):
        return Blog.objects.all().order_by('id')
    
    def location(self, item):
        return reverse('blog_content', args=[item.slug])
    
    def lastmod(self, item):
        return item.modified_date

class Static_Sitemap4(Sitemap):

    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)