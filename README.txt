# Documentation Uploader 0.10 README

## Introduction
DocUp: Automatically get your Markup text files on to PyPI

DocUp uses Markup to convert text files in Markup format to HTML,
put them into a zip folder, and upload the whole thing to PyPI

## Prerequisites

* Python 2.4.3 or newer
* Markdown 1.0.1
* Zip 2.31

Download and compile Python 2.4.3:

    $ VERSION=2.4.3
    $ mkdir /tmp/src 
    $ cd /tmp/src/
    $ wget http://python.org/ftp/python/$VERSION/Python-$VERSION.tar.bz2
    $ tar xjf Python-$VERSION.tar.bz2
    $ rm Python-$VERSION.tar.bz2
    $ cd Python-$VERSION 
    $ ./configure
    $ make
    $ sudo make altinstall

Now we need to install Python setuputils:

    $ cd /tmp/src
    $ wget http://pypi.python.org/packages/2.4.3/s/setuptools/setuptools-0.6c11-py2.4.3.egg
    $ sudo sh setuptools-0.6c11-py2.7.egg

Now install pip to install the rest of our dependencies:

    $ sudo easy_install pip

Now we install Markdown:

    $ sudo pip install markdown

Zip should be pre-installed, but to install it on Redhat-derived distros, use:

    $ sudo yum install zip

or, on Debian-based distros:

    $ sudo apt-get install zip

on Debian-derived distros.

And now for DocUp itself:
 
    $ sudo pip install DocUp


##Syntax

In order to upload a file or comma-seperated list of files to PyPI as documentation,
follow this pattern:

   # ./DocUp.py [FILE1,FILE2,...] <project-name> username:password

*FILE1,FILE2... is the comma-seperated list of files (don't include the square brackets)

*<project-name> is the project to which the documentation will be uploaded (don't include the brackets)

*username:password is the username and password of the PyPI user under whom you want to post the documentation (include the colon)

## License

See LICENSE for details.



