try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cmsplugin_simpleslider

version = cmsplugin_simpleslider.__version__

setup(
    name='cmsplugin_simpleslider',
    packages=['cmsplugin_simpleslider'],
    include_package_data=True,
    version=version,
    description="A djangocms carousel slider plugin.",
    author='Christoph Reimers',
    author_email='christoph@superservice-international.com',
    license='BSD License',
    url='https://github.com/creimers/cmsplugin_simpleslider',
    keywords=['djangocms', 'django', 'carousel', 'slider'], 
    install_requires=[
        'django-cms>=3.5',
        'django-filer>=1.3.0',
        'cmsplugin_filer>=1.0.0',
        'django-admin-sortable>=2.1.0',
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
