FROM 127.0.0.1.nip.io/development/python:latest
WORKDIR /usr/src/app
COPY flask-api/ ./
RUN pip install -r requirements.txt
# Running Unit TESTS
RUN ["make", "test"] # Becouse we need make we cant use the python slim
CMD ["python", "run_app.py"]