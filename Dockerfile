# python 3.8 설치
FROM python:3.8
# 장고 파일 설치경로
WORKDIR /usr/src/app

# packages 설치
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 


COPY . .

# 포트 설정
# EXPOSE 8000

# CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"] 
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "f4.wsgi:application"] 