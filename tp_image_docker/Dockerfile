FROM python:3.10.14-alpine3.19

VOLUME /tmp

WORKDIR /app

COPY src/requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
ADD src /app

CMD [ "python", "main.py" ]