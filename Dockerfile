FROM python:latest as base


COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
ADD ./sprinkler ./sprinkler
COPY ./app.py .

#### DEBUGGER ####
FROM base as debug
RUN pip install ptvsd
WORKDIR /
CMD python3 -m ptvsd --host 0.0.0.0 --port 5677  --multiprocess app.py 


#### PRODUCTION ####
FROM base as production
WORKDIR /
ENTRYPOINT ["python3"]
CMD ["app.py"]


