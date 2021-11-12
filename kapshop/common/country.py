from django.utils                                   import translation
from django_countries                               import countries


def get_countries_translated(i):

    pays = {}

    language = i.get('language')

    if not language:
        language = 'FR'

    translation.activate(language)

    for country in countries:
        pays[translation.gettext(country.code)] = translation.gettext(country.name)

    return pays


def get_countries_choices_translated(language):

    translation.activate(language)

    pays = [(translation.gettext(country.code), country.name) for country in countries]

    return pays