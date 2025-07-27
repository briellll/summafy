from transformers import pipeline  # type: ignore

from .schemas import SummarizeRequest, SummarizeResponse

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')


def summarize(data: SummarizeRequest):
    try:
        summary_list = summarizer(
            data.text,
            do_sample=data.do_sample,
            max_length=data.max_length,
            min_length=data.min_length,
        )

        if not summary_list:
            raise ValueError('A sumarização retornou vazio')

        result_text = summary_list[0]['summary_text']

        return SummarizeResponse(summary_text=result_text)

    except Exception as erro:
        print(f'Erro na camada do core: {erro}')
        raise
