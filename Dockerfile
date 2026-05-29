FROM python:3.11-slim

# Copy the python script into the container
COPY main.py /main.py

# Execute the python script
ENTRYPOINT ["python", "/main.py"]
