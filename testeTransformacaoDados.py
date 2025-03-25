import pdfplumber
import pandas as pd
import zipfile
import os


def verificar_arquivo(pdf_path):
    if os.path.exists(pdf_path):
        print(f"Arquivo encontrado: {pdf_path}")
        return True
    else:
        print(f"Arquivo {pdf_path} não foi encontrado!")
        return False


def extrair_dados_pdf(pdf_path):
    dados = []

    with pdfplumber.open(pdf_path) as pdf:

        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                for linha in tabela:
                    dados.append(linha)

    return dados


def substituir_abreviacoes(dados):
    legenda_abreviacoes = {
        'OD': 'Odontológico',
        'AMB': 'Ambulatorial'
    }


    for i in range(len(dados)):
        for j in range(len(dados[i])):
            if dados[i][j] in legenda_abreviacoes:
                dados[i][j] = legenda_abreviacoes[dados[i][j]]

    return dados


def salvar_csv(dados, nome_arquivo):

    df = pd.DataFrame(dados[1:], columns=dados[0])
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f"Dados salvos em {nome_arquivo}")


def compactar_csv(nome_arquivo):
    zip_nome = f"Teste_{os.getlogin()}.zip"
    with zipfile.ZipFile(zip_nome, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(nome_arquivo, os.path.basename(nome_arquivo))
    print(f"Arquivo compactado como {zip_nome}")


pdf_path = r'C:\Users\Admin\PycharmProjects\ScrappingPython\anexos\Anexo_I.pdf'  # Altere para o caminho correto do seu arquivo PDF


if verificar_arquivo(pdf_path):

    dados_extraidos = extrair_dados_pdf(pdf_path)

    if not dados_extraidos:
        print("Nenhuma tabela encontrada no PDF!")
    else:

        dados_processados = substituir_abreviacoes(dados_extraidos)

        csv_nome = "rol_procedimentos.csv"
        salvar_csv(dados_processados, csv_nome)

        compactar_csv(csv_nome)

        os.remove(csv_nome)
