#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

export FLASK_APP=microblog.py
export FLASK_ENV=development
export FLASK_DEBUG=1

flask db init
# flask db migrate -m "users table"
# flask db migrate -m "posts table"
# flask db migrate -m "organisations table"
# flask db migrate -m "platforms table"
flask db upgrade

pip show flask
pip show flask-login

# python3 seed.py shell
# flask run --host=0.0.0.0 --port=5000
flask run --host=0.0.0.0
