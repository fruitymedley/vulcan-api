FROM python:3.13.2-slim-bookworm

RUN pip install pipenv

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

WORKDIR /src

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]