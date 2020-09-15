FROM python:3.6
COPY . /appl
WORKDIR /appl
RUN pip install -r requirements.txt
EXPOSE 8090
CMD ["gunicorn", "-b", "0.0.0.0:8090", "wsgi"]