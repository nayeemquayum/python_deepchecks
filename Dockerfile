#FROM command to create a base (parent) image.
FROM python:3.10.14
#WORKDIR command to indicate the working directory of the docker container.
#After setting the app directory as the working directory for docker, all the
#rest of the commands will be run under that directory
WORKDIR /app
#COPY all the files from development working directory to the container working directory.
COPY . .
#Install all the dependencies (listed in “requirements.txt”) in the container environment.
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#Using EXPOSE command we provide port information using which we can communicate with the container.
#If our applicat is a web app, it wll have it's own ip and port. However, that port would be
#only accesible within the container. So we need to a provide a port to comunicate to the container (which we could access from localhost)
#This exposed port will be mapped to the internal port of the web application.
EXPOSE 4000
#Using CMD we provide instruction how to run our app from the container
CMD [“python”,“main.py”]