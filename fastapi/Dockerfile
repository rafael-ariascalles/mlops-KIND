FROM python:3.10
WORKDIR /server
EXPOSE 8081
COPY ./requirements.txt /server/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt
COPY ./app /server/app
# Given that wordir has setup to server it will be inside /server/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]