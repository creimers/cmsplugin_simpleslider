try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cmsplugin_simpleslider

version = cmsplugin_simpleslider.__version__

setup(
    name = 'cmsplugin_simpleslider',
    packages = ['cmsplugin_simpleslider'],
    include_package_data = True,
    version = version,
    description = "A djangocms carousel slider plugin.",
    author = 'Christoph Reimers',
    author_email = 'christoph@superservice-international.com',
    license='BSD License',
    url = 'https://github.com/creimers/cmsplugin_simpleslider',
    keywords = ['djangocms', 'django', 'carousel', 'slider'], 
    install_requires = [
        'django-cms>=3.0',
        'django-filer',
        'cmsplugin_filer',
    ],
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
