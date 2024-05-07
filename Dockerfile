FROM python:3.12.3-slim-bookworm

WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command to run the application
CMD ["python", "backend/main.py"]
# CMD ["python", "test_api.py"]
