FROM python:3
WORKDIR /app
COPY movies_app.py /app
COPY movies_app_test.py /app
RUN pip install pytest
RUN pytest