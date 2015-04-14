# djangocms slider plugin

A djangocms carousel slider plugin.

## Installation

* ``pip install git+ssh://git@github.com/creimers/cmsplugin_simpleslider.git``

* add
  ```
  filer,
  easy_thumbnails,
  cmsplugin_simpleslider,
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
