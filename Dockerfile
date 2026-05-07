# Dockerfile
FROM python:3.10

WORKDIR /app

# Install ping (and clean up to keep image small)

#RUN apt-get update && \
#    apt-get install -y iputils-ping && \
#    rm -rf /var/lib/apt/lists/*


# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
