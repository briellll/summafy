from http import HTTPStatus

from fastapi import FastAPI

from .core import summarize
from .schemas import SummarizeRequest, SummarizeResponse

app = FastAPI()


@app.post(
    '/resumir', status_code=HTTPStatus.OK, response_model=SummarizeResponse
)
def summarize_text(payload: SummarizeRequest):
    return summarize(payload)
