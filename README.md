# QuadFile Version 2

A temporary (or permanent, depending on configuration) file sharing service written in Flask.

## Features

* Automatically remove files that aren't accessed often enough
* Supports all filetypes, with options to filter by mimetypes
* Prevents duplicate filenames
* Works on all platforms (as long as they can use basic JavaScript)
* Both easy to set up and use
* Threaded for effective use of resources (Unless you're not on SSD, in which case, enjoy your I/O clogs m8)
* Color-coded and real-time console log
* Easy to use with most applications, such as ShareX

## Requirements

Needed:

* Python 3 (Required for python-magic)
* sqlite3 package for your OS (To create the database)
* Install flask, currently that should be the only requirement and hopefully forever (``pip install -r requirements.txt``)
* python-magic - For the mimetype filtering

Recommended:

* nginx, great for proxy_pass
* gunicorn, allows you to use QuadFile with multiple workers

## Using the thing

## Test deployment

* Clone the repo somewhere
* ``pip install -r requirements.txt``
* Do ``cp conf.py.sample conf.py``
* Edit ``conf.py`` so that the information is correct
* ``sqlite3 files.db < schema.sql``
* ``chmod +x run.py`` and then ``./run.py``
* ???
* PROFIT (Hopefully)

## Production deployment

* Clone the repo somewhere
* Set up a virtual environment for QuadFile
* ``pip install -r requirements.txt``
* Do ``cp conf.py.sample conf.py``
* Edit ``conf.py`` so that the information is correct
* ``sqlite3 files.db < schema.sql``
* ``gunicorn wsgi:app -w 4 --bind 127.0.0.1:8282 --log-file $HOME/quadfile.log`` (Use supervisor to run it on boot if needed)
* Configure nginx and proxy_pass it to gunicorn
* ???
* PROFIT (Hopefully)
