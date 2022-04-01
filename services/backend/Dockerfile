FROM gitlab.sdu.dk:5050/odw-e2020/docker:python-latest

WORKDIR /backend

COPY requirements.txt /backend

RUN pip install -r requirements.txt

COPY app.py /backend

CMD ["python", "app.py"]