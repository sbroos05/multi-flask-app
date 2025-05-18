#!/bin/sh
export FLASK_APP=wsgi.py
flask db upgrade
