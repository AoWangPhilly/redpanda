FROM dockershelf/latex:full
COPY . /app
RUN ["pip", "install -r /app/redpanda/requirements.txt"]
CMD ["cd", "/app/redpanda && python3 src/bot.py"]