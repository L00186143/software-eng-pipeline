FROM python:3.12

WORKDIR /app

COPY . /app

CMD ["python", "calc.py"]