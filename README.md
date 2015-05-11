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
