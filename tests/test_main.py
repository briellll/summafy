from http import HTTPStatus
from unittest.mock import patch

from fastapi.testclient import TestClient

from src.summafy.main import app
from src.summafy.schemas import SummarizeResponse

client = TestClient(app)


def test_endpoint_resumir_com_sucesso():
    dados_payload = {
        'text': 'Este é um texto para ser resumido pelo endpoint.'
    }

    retorno_mock = SummarizeResponse(
        summary_text='Texto resumido pelo mock da API.'
    )

    with patch('src.summafy.main.summarize', return_value=retorno_mock):
        response = client.post('/resumir', json=dados_payload)

        assert response.status_code == HTTPStatus.OK

        assert response.json() == {
            'summary_text': 'Texto resumido pelo mock da API.'
        }
