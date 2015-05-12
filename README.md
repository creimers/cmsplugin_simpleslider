[![Build Status](https://travis-ci.org/creimers/cmsplugin_simpleslider.svg?branch=master)](https://travis-ci.org/creimers/cmsplugin_simpleslider)
[![Coverage Status](https://coveralls.io/repos/creimers/cmsplugin_simpleslider/badge.svg?branch=develop)](https://coveralls.io/r/creimers/cmsplugin_simpleslider?branch=develop)
[![Code Climate](https://codeclimate.com/github/creimers/cmsplugin_simpleslider/badges/gpa.svg)](https://codeclimate.com/github/creimers/cmsplugin_simpleslider)
[![Requirements Status](https://requires.io/github/creimers/cmsplugin_simpleslider/requirements.svg?branch=master)](https://requires.io/github/creimers/cmsplugin_simpleslider/requirements/?branch=master)
<!--[![Latest Version](https://pypip.in/version/cmsplugin_simpleslider/badge.svg)](https://pypi.python.org/pypi/cmsplugin-simpleslider/)-->
<!--[![Supported Python versions](https://pypip.in/py_versions/cmsplugin_simpleslider/badge.svg)](https://pypi.python.org/pypi/cmsplugin-simpleslider/)-->
<!--[![Development Status](https://pypip.in/status/cmsplugin_simpleslider/badge.svg)](https://pypi.python.org/pypi/cmsplugin_simpleslider/)-->

# djangocms slider plugin

A djangocms carousel slider plugin.


## Installation

* ``pip install cmsplugin_simpleslider``

* add

  ```
  'filer',
  'easy_thumbnails',
  'cmsplugin_filer_image',
  'django-admin-sortable',
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

* for django >= 1.7: add 

  ```
  'filer': 'filer.migrations_django',
  'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
  'cmsplugin_simpleslider': 'cmsplugin_simpleslider.migrations_django',
  ```
  to ``MIGRATION_MODULES``.

  Also check the django 1.7 settings of [filer](https://github.com/stefanfoulis/django-filer#django-17).
