FROM dockershelf/latex:full

RUN apt-get update && apt-get install -y \
    python3.6 \
    python3-pip

COPY . /redpanda

WORKDIR /redpanda

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "src/bot.py"]