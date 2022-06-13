import os

import uvicorn
from fastapi import FastAPI, BackgroundTasks

from strategies import Strategy, SendTextConsole, SendTextKafka
from utils import read_from_api, from_kafka

app = FastAPI()


@app.get("/")
async def root():
    return 'ok'


@app.get("/api/")
async def process(file_url: str, background_tasks: BackgroundTasks):
    strategy = os.getenv('STRATEGY', default='console')
    background_tasks.add_task(main, file_url, strategy)
    return f"Processing started. File: '{file_url}'"


async def main(file_url: str, strategy: Strategy):
    text = read_from_api(file_url)
    if strategy == Strategy.CONSOLE:
        SendTextConsole.send_text(text)
        print('text was sent to console')
    elif strategy == Strategy.KAFKA:
        SendTextKafka.send_text(text)
        print('text was sent to kafka')
    else:
        print(f'no such strategy: {strategy}')


if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='localhost')
