FROM python:3.12-slim
WORKDIR /app
COPY quiz_system.py .
RUN useradd --create-home app
USER app
CMD ["python", "quiz_system.py"]
