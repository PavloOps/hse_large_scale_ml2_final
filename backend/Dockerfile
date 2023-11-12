FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
WORKDIR /app
RUN mkdir -p /app/model
COPY backend_api.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN wget https://github.com/PavloOps/lsml2/releases/download/v1.0.0/pytorch_model.bin -P /app/model
RUN wget https://github.com/PavloOps/lsml2/releases/download/v1.0.0/training_args.bin -P /app/model
RUN wget https://github.com/PavloOps/lsml2/releases/download/v1.0.0/config.json -P /app/model
EXPOSE 5000
ENV FLASK_APP=backend_api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT ["flask", "run"]
