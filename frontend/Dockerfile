FROM python:3.10-slim
WORKDIR /app
COPY materials materials
COPY frontend.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=100 future
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "frontend.py"]