FROM python:alpine

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && \
    pip install pytest

CMD ["pytest", "test_turbidityAnalysis2.py"]
