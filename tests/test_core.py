from unittest.mock import patch

import pytest

from src.summafy.core import summarize
from src.summafy.schemas import SummarizeRequest, SummarizeResponse

TEXTO_EXEMPLO = (
    'A inteligência artificial generativa representa uma revolução '
    'significativa. Modelos de linguagem extensos, conhecidos como LLMs, '
    'são treinados em vastos conjuntos de dados, o que lhes confere a '
    'capacidade de compreender padrões complexos. Esses sistemas podem '
    'executar tarefas criativas como escrever artigos e sintetizar '
    'documentos longos em resumos coesos e informativos.'
)


def test_summarize_com_sucesso():
    dados_requisicao = SummarizeRequest(
        text=TEXTO_EXEMPLO, min_length=20, max_length=50
    )

    retorno_mock = [
        {'summary_text': 'IA generativa é uma revolução que resume textos.'}
    ]

    with patch(
        'src.summafy.core.summarizer', return_value=retorno_mock
    ) as mock_summarizer:
        resultado = summarize(dados_requisicao)

        mock_summarizer.assert_called_once()

        mock_summarizer.assert_called_with(
            dados_requisicao.text,
            do_sample=dados_requisicao.do_sample,
            max_length=dados_requisicao.max_length,
            min_length=dados_requisicao.min_length,
        )

        assert isinstance(resultado, SummarizeResponse)
        result = 'IA generativa é uma revolução que resume textos.'
        assert resultado.summary_text == result


def test_summarize_lida_com_resultado_vazio():
    dados_requisicao = SummarizeRequest(text='texto curto')
    retorno_mock_vazio = []

    with patch('src.summafy.core.summarizer', return_value=retorno_mock_vazio):
        with pytest.raises(ValueError, match='A sumarização retornou vazio'):
            summarize(dados_requisicao)
