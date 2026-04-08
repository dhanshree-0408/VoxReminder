# 1. Use a lightweight Python 3.10 image
FROM python:3.10-slim

# 2. Install system-level dependencies for Audio (Whisper needs ffmpeg)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy your project files into the container
COPY . .

# 5. Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 6. Expose the port Streamlit runs on
EXPOSE 8501

# 7. Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]