sudo apt-get update
sudo apt-get install python3.4-venv
python3 -m venv env
source env/bin/activate

pip install sqlalchemy psycopg2

sudo service postgresql start

