FROM python:3.6

WORKDIR /app

COPY . .
 
RUN pip install -r requirements.txt
RUN printenv connectionstring

EXPOSE 5000

#ARG connectionstring
ENV DATABASE_URI=${connectionstring}

ENTRYPOINT [ "python", "app.py" ]