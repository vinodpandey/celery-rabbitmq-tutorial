from time import sleep
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://user:password@rabbitmq:5672')


@app.task
def calculate_prime(limit):
    result = list()
    if limit > 1:
        for num in range(2, limit):
            sleep(10)
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result.append(str(num))
    return ", ".join(result)


