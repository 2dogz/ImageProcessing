FROM python:3-onbuild


RUN pip install --upgrade pip && \
    pip install -r requirements.txt &&

CMD ["python", "./hello.py"]
