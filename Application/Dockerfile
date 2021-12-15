FROM python:3.6

WORKDIR /app

COPY . .
 
RUN pip install -r requirements.txt

EXPOSE 5000

ARG DATABASE_URI

ENTRYPOINT [ "python", "app.py" ]