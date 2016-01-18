import tweepy
import requests

from instagram.client import InstagramAPI

from socialfeedsparser.contrib.parsers import ChannelParser, PostParser
from socialfeedsparser.contrib.instagram.settings import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_CLIENT_SECRET
from socialfeedsparser.utils import url_regex
from .settings import (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                       TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKENS_SECRET)


class TwitterSource(ChannelParser):
    """
    Collect class for tweeter.
    """

    name = 'Twitter'
    slug = 'twitter'

    def get_messages_user(self, screen_name, count=20):
        """
        Return tweets from user feed.

        :param screen_name: screen name of the user feed to parse.
        :type item: str

        :param count: number of items to retrieve (default 20).
        :type item: int
        """
        return self.get_api().user_timeline(
            screen_name=screen_name, count=count,
            include_entities=True, include_rts=False)

    def get_messages_search(self, search):
        """
        Return tweets by search param.

        :param search: search string to search for on twitter.
        :type item: str
        """
        return self.get_api().search(
            q=search, include_entities=True, result_type='mixed',
            count=self.channel.limit)

    def get_api(self):
        """
        Return authenticated connections with twitter.
        """
        oauth = tweepy.OAuthHandler(
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET)
        oauth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKENS_SECRET)
        return tweepy.API(oauth)

    def get_instagram_api(self):
        """
        Return authenticated connections with Instagram.
        """
        api = InstagramAPI(access_token=INSTAGRAM_ACCESS_TOKEN,
                           client_secret=INSTAGRAM_CLIENT_SECRET)
        return api

    def get_instagram_image(self, message):
        """
        Return the link to the image of Instagram.
        """
        # check if link in content goes to instagram and save that image
        results = url_regex.findall(message)

        if len(results) > 0:
            # get the last result, it most likely to be the image
            url = results[len(results)-1]
            if not url.startswith('http'):
                url = "http://%s" % url

            session = requests.Session()  # so connections are recycled
            resp = session.head(url, allow_redirects=True)

            if 'instagram' in resp.url:
                # get shortcode
                splitted = resp.url.split('/')  # splitting https://www.instagram.com/p/DFGFH24S2/

                if len(splitted) > 0:
                    shortcode = splitted[len(splitted)-2]

                    try:
                        result = self.get_instagram_api().media_shortcode(shortcode=shortcode)
                        # return image_url, video_url
                        return result.images['standard_resolution'].url,
                        result.videos['standard_resolution'].url if hasattr(result, 'videos') else None
                    except:
                        pass

        return None, None

    def prepare_message(self, message, channel):
        """
        Convert tweets to standard message.

        :param message: message entry to convert.
        :type item: dict
        """

        # I assume there is only one video or image
        video_url = None
        image_url = None
        if 'media' in message.entities:
            url = message.entities['media'][0]['expanded_url']
            image_url = message.entities['media'][0]['media_url']

            if '/video/' in url:
                # extended_entities are not in the search JSON yet..
                # Get the tweet via the status JSON and retrieve the video url from there.
                status = self.get_api().get_status(id=message.id)
                if hasattr(status, 'extended_entities'):
                    try:
                        # get mp4
                        for video in status.extended_entities['media'][0]['video_info']['variants']:
                            if video['url'].endswith('mp4'):
                                video_url = video['url']
                    except:
                        pass
        else:
            # Check of there's an instagram image in the content.
            # It's blocked by twitter itself so it's not in de media entities.
            image_url, video_url = self.get_instagram_image(message.text)

        return PostParser(
            uid=message.id_str,
            author=message.user.name,
            author_uid=message.user.screen_name,
            avatar=message.user.profile_image_url,
            content=message.text,
            date=message.created_at,
            image=image_url,
            video=video_url,
            link='https://twitter.com/%s/status/%s' % (
                message.user.screen_name, message.id_str)
        )
