FROM 744628107553.dkr.ecr.us-east-1.amazonaws.com/my-python-base-app:python3.10-slim
COPY ecs_app.py /ecs_app.py
COPY welcome.gif /welcome.gif
CMD ["python", "/ecs_app.py"]
