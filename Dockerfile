  
FROM python:latest  

 
WORKDIR /code  

  
COPY requirements.txt /code/  


RUN pip install --no-cache-dir -r requirements.txt  

  
COPY . /code/  

  
EXPOSE 8000  


CMD ["gunicorn", "Roshan.wsgi:application", "--bind", "0.0.0.0:8000"]
