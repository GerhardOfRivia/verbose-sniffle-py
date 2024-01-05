# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install

# Make port 80 available to the world outside this container
EXPOSE 80

# Run your application
CMD ["poetry", "run", ".py"]
