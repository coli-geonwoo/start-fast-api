
"""
def vs async def
- await를 호출하도록 가이드하는 third party 라이브러리 사용시 async def 사용
- def인 경우에도 비동기로 동작
- 비동기 코드를 코루틴으로 async와 await로 지원
"""
import time

from fastapi import FastAPI


#잘못된 예제

app = FastAPI()

async def some_lib(num: int, something:str):
    s =0
    for i in range(num):
        print("something.. : " , something, i)
        time.sleep(1)
        s+=1
    return s

@app.post("/")
async def read_results(something:str):
    s1= await some_lib(5, something)
    return {
        "data" : "data",
        "s1" : s1
    }


