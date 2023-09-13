"# Graduatework" 

# celery -A checker beat --loglevel=INFO
# celery -A checker worker --loglevel=INFO
pip install pytest-cov
pytest --cov=src --cov-report=html
pytest --cov