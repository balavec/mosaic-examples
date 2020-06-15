from setuptools import setup, find_packages

version = "0.1"

long_description = (open('README.rst').read())

setup(
    name='pwc',
    version=version,
    description="",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
    keywords='',
    author='Six Feet Up, Inc',
    author_email='info@sixfeetup.com',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['pwc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'sixfeetup.utils>=2.8',
        'Plone',
        'plone.api',
        'z3c.jbot',
        'plone.app.themingplugins',
        'plone.app.mosaic',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
