import tweepy

from socialfeedsparser.contrib.parsers import ChannelParser, PostParser
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
                # print '>>> VIDEO FOUND ??'
                # extended_entities are not in the search JSON yet..
                # Get the tweet via the status JSON and retrieve the video url from there.
                status = self.get_api().get_status(id=message.id)
                if 'extended_entities' in status:
                    try:
                        print status
                        video_url = status['extended_entities']['video_info']['variants'][0]['url']
                    except:
                        pass

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
