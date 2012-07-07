git pull --all
pip install -r pip-req.txt
./manage.py syncdb
./manage.py migrate --all