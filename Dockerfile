# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential vlc

# Copy project requirements
COPY requirements.txt /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create Directory for uploads and file serving point
RUN mkdir uploads 

# Copy the current directory contents into the container at /code
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
