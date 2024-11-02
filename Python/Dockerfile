FROM python:3.9

WORKDIR /app

COPY app.py /app

RUN pip install flask netifaces  # Change 'netiface' to 'netifaces'

EXPOSE 8000

CMD ["python", "app.py"]
