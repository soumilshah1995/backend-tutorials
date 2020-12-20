FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

#It's important to copy the app code after installing the dependencies, that way you can take advantage of Docker's cache. That way it won't have to install everything from scratch every time you update your application files, only when you add new dependencies.
#This also applies for any other way you use to install your dependencies. If you use a requirements.txt, copy it alone and install all the dependencies on the top of the Dockerfile, and add your app code after it.
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

#RUN pip install fastapi uvicorn
#RUN pip install -r requirements.txt

#Placed docker in the parent directory as its not required to run 
#and only moving the app contents which is in main.py
#Also changed the yaml

COPY ./project /app/app

#Not required as its handled by above Base Image
#CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]