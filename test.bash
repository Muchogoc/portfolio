#!/bin/bash

exec gunicorn -c config.py portfolio.wsgi:application