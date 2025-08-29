# 📄 Analisador de Texto em PDF

🚧 Projeto em Desenvolvimento 🚧

Este projeto em Python oferece funções para extrair texto de arquivos PDF e realizar análise de frequência de palavras, letras e pontuação.

🛠️ Funcionalidades

extrair_pdf(arquivo_pdf_local): Extrai o texto de um arquivo PDF e retorna esse texto em formato string.

analisar_texto(texto): Analisa um texto e retorna contagem de palavras, de letras, frequência de palavras, de letras e de pontuação. Essa função não necessita de um arquivo em PDF, somente uma variável (str).

🚀 Como Usar

1.Instale o arquivo analisar_texto.py
2.Instale a biblioteca necessária:
  pip install pymupdf
3.Utilize as funções no seu código:
  from analisador_texto import extrair_pdf, analisar_texto
  
  texto = extrair_pdf('seuarquivo.pdf')
  resultado = analisar_texto(texto)
  
  print('Total de palavras:', resultado['total_palavras'])
  print('10 palavras mais comuns:', resultado['frequencia_palavras'].most_common(10))

🧪 Tecnologias Utilizadas

- Python 3.x
- PyMuPDF (para extração de texto de PDFs)
- string.punctuation (para verificar a lista de pontuações)
- collections.Counter (para análise de frequência)

👤 Autor:
RodolphoAra

📝 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
