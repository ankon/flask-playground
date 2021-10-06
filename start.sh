#!/bin/sh

. venv/bin/activate

FLASK_APP=main FLASK_ENV=development flask run