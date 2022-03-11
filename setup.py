import os

from setuptools import find_packages, setup

# circleci.py version
VERSION = "1.1.6"

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='portfolio website',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='A simple portfolio website for showcasing my projects. ',
    long_description=open('README.md').read(),
    author='Charles Muchogo',
    author_email='muchogoc@gmail.com.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django==2.2.8",
        "django-environ==0.4.5",
        "django-tastypie==0.9.15",
        "Pillow==9.0.1",
        "psycopg2==2.8.3",
        "setproctitle==1.1.10",
        "django-prometheus==1.0.15",
        "sentry-sdk==0.10.0",
        "gunicorn==19.9.0",
    ],
    python_requires='>=3',

)
