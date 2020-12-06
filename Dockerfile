FROM python:3 
COPY . . 
RUN pip install Django>=3.0
RUN pip install psycopg2-binary>=2.8
ENTRYPOINT [ "python", "manage.py", "runserver" ]