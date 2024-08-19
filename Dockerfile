FROM python:3.8

# Set the working directory in the container
WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .
COPY templates/index.html ./templates/


EXPOSE 80


CMD ["python", "app.py"]