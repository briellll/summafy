from pydantic import BaseModel, Field


class SummarizeResponse(BaseModel):
    summary_text: str


class SummarizeRequest(BaseModel):
    text: str = Field(..., description='texto a ser resumido')
    do_sample: bool = Field(
        default=False, description='se deve gerar com amostragem'
    )
    max_length: int = Field(
        default=130, ge=10, le=512, description='tamanho maximo do resumo'
    )
    min_length: int = Field(
        default=30, ge=0, le=500, description='tamanho minimo do resumo'
    )
