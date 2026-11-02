FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask scikit-learn numpy joblib

EXPOSE 5000

CMD ["python", "app.py"]