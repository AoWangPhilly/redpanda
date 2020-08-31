FROM dockershelf/latex:full
COPY . /app
CMD ["python3", "/app/src/bot.py"]