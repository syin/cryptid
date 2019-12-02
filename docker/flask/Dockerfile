FROM python:3.6-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /code
WORKDIR /code

# TODO SY 4 workers in prod only
# CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8001", "server:app"]
CMD ["gunicorn", "-b 0.0.0.0:8001", "server:app"]