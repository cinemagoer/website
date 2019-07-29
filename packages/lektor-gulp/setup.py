from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    readme = fh.read()

setup(
    name='lektor-gulp',
    version='0.3.2',
    author=u'Maurizio Turatti',
    author_email='maurizio@softinstigate.com',
    description=u'A simple Lektor plugin for gulp',
    url = "https://github.com/SoftInstigate/lektor-gulp",
    license='BSD',
    keywords='Lektor gulp plugin static-site CMS',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['lektor_gulp'],
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'lektor.plugins': [
            'gulp = lektor_gulp:GulpPlugin',
        ]
    }
)
