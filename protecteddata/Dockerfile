FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /protecteddata
COPY req.txt /protecteddata/
EXPOSE 8000
RUN pip install -r req.txt
COPY . /protecteddata/