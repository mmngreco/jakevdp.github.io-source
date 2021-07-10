#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Maximiliano Greco'
SITENAME = 'mmngreco'
SITEURL = ''
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "theme"
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    nb_markup,
    # 'summary',       # auto-summarizing articles
    # 'feed_summary',  # use summaries for RSS, not full articles
]

ENABLE_MATHJAX = True

PATH = 'content'
STATIC_PATHS = ['images', 'figures', 'favicon.ico']
ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'mmngreco'
GITHUB_USERNAME = 'mmngreco'
STACKOVERFLOW_ADDRESS = 'https://stackoverflow.com/users/3124367/mmngreco'
AUTHOR_WEBSITE = 'https://mmngreco.github.io'
AUTHOR_BLOG = 'https://mmngreco.github.io'
# AUTHOR_CV = "http://staff.washington.edu/mmngreco/media/pdfs/CV.pdf"
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds
IGNORE_FILES = [".ipynb_checkpoints"]

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
