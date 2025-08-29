def extrair_pdf(arquivo_pdf_local) -> str:
    """
    Extrai o texto de um arquivo .pdf e retorna esse texto em formato (str)

    Args:
    caminho_pdf (pdf): arquivo pdf a ser lido

    Returns:
        texto (str): texto extraído do pdf

    Requisitos:
        Instalar a biblioteca PyMuPDF:
            pip install pymupdf
    """
    import fitz #necessário pymupdf
    with fitz.open(arquivo_pdf_local) as doc:
        texto = ''
        for pagina in doc:
            texto += pagina.get_text()
    return texto

def analisar_texto(texto: str):
    from string import punctuation
    from collections import Counter
    """
    Analisa um texto e retorna contagem de palavras, frequência de palavras, 
    de letras e de pontuacao.

    Args:
        texto (str): Texto a ser analisado.

    Returns:
        dict:
            - total_palavras (int): número total de palavras do texto.
            - total_letras (int): número total de letras do texto.
            - frequencia_palavras (Counter): frequência de cada palavra.
            - frequencia_letras (Counter): frequência de cada letra(com diferença em caso de acentuação).
            - frequencia_pontuacao (Counter): frequência de cada caractere de pontuação.

    """
    pontuacao = punctuation + '-' + '–'
    texto_sempontuacao = [palavra.strip(pontuacao) for palavra in texto.split() if palavra.strip(pontuacao)]
    frequencia_letras = Counter(letra.lower() for palavra in texto_sempontuacao for letra in palavra)
    return {
        'total_palavras': len(texto_sempontuacao),
        'total_letras': sum(frequencia_letras.values()),
        'frequencia_palavras': Counter(texto_sempontuacao), 
        'frequencia_letras': frequencia_letras, 
        'frequencia_pontuacao': Counter(letra for palavra in texto.split() for letra in palavra if letra in pontuacao)
    }
