import hashlib

from instagram.client import InstagramAPI

from .settings import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_CLIENT_SECRET
from socialfeedsparser.contrib.parsers import ChannelParser, PostParser


class InstagramSource(ChannelParser):
    """
    Collect class for Instagram.
    """

    name = 'Instagram'
    slug = 'instagram'

    def get_messages_user(self, user_id):
        """
        Return posts from user feed.

        :param user_id: user id of the feed to parse.
        :type item: str

        :param count: number of items to retrieve (default 20).
        :type item: int
        """
        api = self.get_api()
        user = api.user_search(q=user_id)[0].id
        return api.user_recent_media(user_id=user)[0]

    def get_messages_search(self, search):
        """
        Return posts by search param.

        :param search: search string to search for on Instagram.
        :type item: str
        """
        api = self.get_api()
        return api.tag_recent_media(tag_name=search)[0]

    def get_api(self):
        """
        Return authenticated connections with Instagram.
        """
        api = InstagramAPI(access_token=INSTAGRAM_ACCESS_TOKEN,
                           client_secret=INSTAGRAM_CLIENT_SECRET)
        return api

    def prepare_message(self, message, channel):
        """
        Convert posts to standard message.

        :param message: message entry to convert.
        :type item: dict
        """
        return PostParser(
            uid=hashlib.sha224(message.id).hexdigest()[:50],
            author=message.user.username,
            author_uid=message.user.username,
            avatar=message.user.profile_picture,
            content=message.caption.text,
            date=message.created_time,
            image=message.images['standard_resolution'].url,
            video=message.videos['standard_resolution'].url if hasattr(message, 'videos') else None,
            link=message.link
        )
