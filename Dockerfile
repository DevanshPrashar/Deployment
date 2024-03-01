FROM python:3.9
WORKDIR /1
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "1.py"]
