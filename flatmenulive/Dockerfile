FROM python:3.10-slim
WORKDIR /apps
COPY ./r.txt .
RUN pip install -r r.txt --no-cache-dir
COPY . .
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]