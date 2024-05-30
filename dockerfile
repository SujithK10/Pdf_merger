# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies (if any)
# If your main.py requires any specific dependencies, add them here
# RUN pip install --no-cache-dir <dependency>

# Run main.py to merge PDF files
CMD ["python", "main.py", "North India.pdf", "South India.pdf", "merged_document.pdf"]
