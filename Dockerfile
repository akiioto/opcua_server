FROM python:3.8

WORKDIR /usr/app/src

COPY run_server.py ./

RUN pip install asyncua
RUN pip install opcua
RUN pip install asyncio

CMD [ "python", "run_server.py"]
EXPOSE 4840