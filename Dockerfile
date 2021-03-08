FROM python:latest


COPY ./app.py .
COPY ./requirements.txt .
ADD ./sprinkler ./sprinkler
RUN pip3 install -r requirements.txt


#RUN python3 /sprinkler/initialize_db.py

WORKDIR /

ENTRYPOINT ["python3"]
CMD ["app.py"]


