from setuptools import setup

setup(
    name='gfm',
    version='0.0.1',
    description='Convert GitHub-Flavored Markdown to HTML',
    long_description=open('README.rst').read(),
    url='http://github.com/stewart/gfm/',
    license=open('LICENSE').read(),
    author='Andrew Stewart',
    author_email='andrew@stwrt.ca',
    py_modules=['gfm'],
    include_package_data=True,
    install_requires=['markdown'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
