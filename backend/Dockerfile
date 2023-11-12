FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
WORKDIR /app
COPY model model
COPY backend_api.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=backend_api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT ["flask", "run"]