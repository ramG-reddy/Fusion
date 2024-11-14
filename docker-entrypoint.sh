echo "Starting Fusion-IIIT server"

python FusionIIIT/manage.py makemigrations && \
python FusionIIIT/manage.py migrate && \
python FusionIIIT/manage.py runserver 0.0.0.0:8000
