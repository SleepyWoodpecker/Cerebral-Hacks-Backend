# Use Python 3.10 image as the base image
FROM python:3.10

# Get requirements and install
COPY requirements.txt .

# Install dependencies
RUN pip install wheel
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# COPY the data, src and evaluator folder
COPY /src ./src
COPY /evaluator ./evaluator
COPY /data ./data

# copy environment variables
# COPY .env .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["fastapi", "run", "src/main.py", "--port", "8080"]
