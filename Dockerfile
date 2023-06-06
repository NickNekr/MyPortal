FROM python:3.9
WORKDIR /web
COPY . /web
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "wsgi.py"]

