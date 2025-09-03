FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY ./app ./app

# Copy database files
COPY ./temp_db_files ./temp_db_files

# Expose port
EXPOSE 8888

# Run app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888"]