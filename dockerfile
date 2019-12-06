FROM python:3.6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt
RUN rm -rf /usr/src/app
COPY . /usr/src/app
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
