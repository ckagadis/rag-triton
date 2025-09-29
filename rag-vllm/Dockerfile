FROM nvidia/cuda:12.1.105-base-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip git

RUN pip3 install vllm

COPY config.json .
COPY start.sh .

EXPOSE 8000
CMD ["bash", "start.sh"]
