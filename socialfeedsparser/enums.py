from django.utils.translation import ugettext_lazy as _


class Language(object):
    DUTCH = 'nl'
    FRENCH = 'fr'
    ENGLISH = 'en'

    choices = (
        (DUTCH, _('Dutch')),
        (FRENCH, _('French')),
        (ENGLISH, _('English')),
    )
