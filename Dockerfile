FROM python:3.6

RUN adduser usr

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

RUN chown -R usr:usr /usr/sbin/adduser

CMD ["python3", "run.py"]