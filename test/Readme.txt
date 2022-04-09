#간단 테스트 방법

#books 테스트
uvicorn books:app --reload

#books2 테스트
uvicorn books2:app --reload

#routertest 테스트
uvicorn routertest:app --reload

#api 테스트
uvicorn main:app --reload
