[![Build Status](https://travis-ci.org/creimers/cmsplugin_simpleslider.svg?branch=master)](https://travis-ci.org/creimers/cmsplugin_simpleslider)
[![Coverage Status](https://coveralls.io/repos/creimers/cmsplugin_simpleslider/badge.svg?branch=master)](https://coveralls.io/r/creimers/cmsplugin_simpleslider?branch=master)
[![Code Climate](https://codeclimate.com/github/creimers/cmsplugin_simpleslider/badges/gpa.svg)](https://codeclimate.com/github/creimers/cmsplugin_simpleslider)
[![Requirements Status](https://requires.io/github/creimers/cmsplugin_simpleslider/requirements.svg?branch=master)](https://requires.io/github/creimers/cmsplugin_simpleslider/requirements/?branch=master)
[![Latest Version](https://img.shields.io/pypi/v/cmsplugin_simpleslider.svg)](https://img.shields.io/pypi/v/cmsplugin_simpleslider.svg)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cmsplugin_simpleslider.svg)](https://img.shields.io/pypi/pyversions/cmsplugin_simpleslider.svg)
[![Status](https://img.shields.io/pypi/status/cmsplugin_simpleslider.svg)](https://img.shields.io/pypi/status/cmsplugin_simpleslider.svg)

# djangocms slider plugin

A djangocms carousel slider plugin based on [slick](http://kenwheeler.github.io/slick/). Requires django>=1.7.


## Installation

* ``pip install cmsplugin_simpleslider``

* add

  ```
  'filer',
  'easy_thumbnails',
  'cmsplugin_filer_image',
  'adminsortable',
  'cmsplugin_simpleslider',
  ```

to ``INSTALLED_APPS``.

* add 

  ```
  THUMBNAIL_PROCESSORS = (
      'easy_thumbnails.processors.colorspace',
      'easy_thumbnails.processors.autocrop',
      'filer.thumbnail_processors.scale_and_crop_with_subject_location',
      'easy_thumbnails.processors.filters',
  )
  ```
to ``settings.py``.

* add 

  ```
  'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
  ```

  to ``MIGRATION_MODULES``

* sync the database
