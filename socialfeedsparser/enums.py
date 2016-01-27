from django.utils.translation import ugettext_lazy as _


class Language(object):
    DUTCH = 'nl'
    ENGLISH = 'en'
    FRENCH = 'fr'
    GERMAN = 'de'
    ITALIAN = 'it'
    SPANISH = 'es'

    choices = (
        (DUTCH, _('Dutch')),
        (ENGLISH, _('English')),
        (FRENCH, _('French')),
        (GERMAN, _('German')),
        (ITALIAN, _('Italian')),
        (SPANISH, _('Spanish')),
    )
