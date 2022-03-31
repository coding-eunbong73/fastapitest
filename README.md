## virtualenv 환경 모듈 설치
pip install venv

## virtualenv 생성
python -m venv fastapienv

## virtualenv 활성화
cd fastapienv/Scripts
activate 실행

## virtualenv 환경에, fastapi 설치
pip install fastapi[all]


## 첫 프로그램 실행 ( virtualenv activate 환경임)
uvicorn books:app --reload

## browser에서 실행
http://localhost:8000/       <-- api 결과
http://localhost:8000/docs   <-- swagger
http://localhost:8000/redoc   <-- API 문서
http://localhost:8000/openapi.json  <-- api spec

