FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install Dependencies
RUN apt-get update
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev gcc
RUN apt-get install -y python-pip

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


EXPOSE 80

# Run twisted-web.py when the container launches
CMD ["python", "twisted-pymodbus.py"]
