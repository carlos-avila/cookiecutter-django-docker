from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

from blog.models import BlogIndexPage, BlogEntryPage


class BlogIndexFeedRSS(Feed):
    feed_type = Rss201rev2Feed

    def get_object(self, request, *args, **kwargs):
        # Only one blog index allowed
        return BlogIndexPage.objects.live().first()

    def title(self, obj):
        return obj.seo_title if obj.seo_title else obj.title

    def link(self, obj):
        return obj.full_url

    def description(self, obj):
        return obj.search_description

    def author_name(self, obj):
        return obj.owner

    def items(self):
        return BlogEntryPage.objects.live().order_by('-date')

    def item_title(self, item):
        return item.seo_title if item.seo_title else item.title

    def item_link(self, item):
        return item.full_url

    def item_description(self, item):
        return item.intro

    def item_author_name(self, item):
        return item.owner

    def item_pubdate(self, item):
        return item.first_published_at

    def item_updateddate(self, item):
        return item.latest_revision_created_at


class BlogIndexFeedAtom(BlogIndexFeedRSS):
    feed_type = Atom1Feed

    def subtitle(self, obj):
        return obj.search_description
