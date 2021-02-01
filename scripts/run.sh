#!/bin/sh
cd ${PYTHONPATH}
celery -A api.job worker --loglevel=INFO &
echo "declare -x PYTHONPATH=$PYTHONPATH"
cd ${PYTHONPATH}/api
CMD flask run --host 0.0.0.0 --port 5100
cd ${PYTHONPATH}/api
python app.py
