# build_files.sh

pip3 install -r requirements.txt
pip3 install Django
python3.9 manage.py collectstatic --noinput