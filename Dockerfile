FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


RUN useradd -r -s /bin/bash johnniefujita

ENV HOME /app

WORKDIR ./

ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R johnniefujita:johnniefujita /app

USER johnniefujita

ENV FAST_API_ENV=production


#ARG AWS_ACCESS_KEY_ID
#ARG AWS_SECRET_ACCESS_KEY
#ARG AWS_DEFAULT_REGION

#ARG FLASK_SECRET_KEY

#ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
#ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
#ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
#ENV FLASK_SECRET_KEY $FLASK_SECRET_KEY


ADD ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user

COPY ./src /app/src
WORKDIR /app


CMD ["uvicorn",  "src.main:app", "--host=0.0.0.0", "--reload", "--port", "8000"]
