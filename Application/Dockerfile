FROM python:3.6

WORKDIR /app

COPY . .
 
RUN pip install -r requirements.txt

EXPOSE 5000

ARG connectionstring
ENV DBI_STRING=${connectionstring}

ENTRYPOINT [ "python", "app.py" ]