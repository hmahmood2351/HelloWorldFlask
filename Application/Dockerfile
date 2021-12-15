FROM python:3.6

WORKDIR /app

COPY . .
 
RUN pip install -r requirements.txt
RUN export connectionstring

EXPOSE 5000

# ARG DATABASE_URI
ENV connectionstring=${connectionstring}

ENTRYPOINT [ "python", "app.py" ]