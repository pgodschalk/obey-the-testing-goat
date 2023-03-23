FROM python:3.6-alpine3.15

RUN adduser -D worker

USER worker

WORKDIR /home/worker

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY --chown=worker:worker requirements.txt requirements.txt

RUN pip install --user --requirement requirements.txt

COPY --chown=worker:worker . .

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver"]

EXPOSE 8000
