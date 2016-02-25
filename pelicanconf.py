#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'neurocoder'
SITENAME = u"neurocoder's notes"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME = 'themes/svbhack'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

LOCALE = "C"
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'
SLUGIFY_SOURCE = 'basename'

DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['static/CNAME', 'static/favicon.jpg']
EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
    'static/favicon.jpg': {'path': 'favicon.ico'}
}

USER_LOGO_URL = '/favicon.ico'
TAGLINE = 'Record my thoughts'
ARTICLE_PATHS = ['posts']
MENUITEMS = [('categories', 'categories.html'),
             ('tags', 'tags.html')]
DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags']   

ARTICLE_URL             = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS         = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARCHIVES_SAVE_AS        = 'posts/index.html'
YEAR_ARCHIVE_SAVE_AS    = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS   = 'posts/{date:%Y}/{date:%m}/index.html'
