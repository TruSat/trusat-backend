#!/bin/bash
gunicorn --workers 4 --bind unix:trusat-backend.sock -u www-data -g www-data -m 007 wsgi:app & 
nginx