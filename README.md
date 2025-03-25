-Este projeto realiza a extração de dados de tabelas contidas em arquivos PDF, processa as informações adicionais abreviadas e salva os dados em formato CSV. Além disso, o CSV gerado é compactado em um arquivo ZIP para facilitar o armazenamento e envio.



FUNCIONALIDADES:

1-Verificação de Arquivo PDF : O projeto verifica se o arquivo PDF fornecido existe.

2-Extração de Dados de Tabelas no PDF: Usando a biblioteca pdfplumber, o projeto extrai tabelas contidas nas páginas do PDF.

3-Substituição de Abreviações : Abreviações presentes nas tabelas como OD e AMB são extintas por seus respectivos significados.

4-Salvamento em CSV : Os dados extraídos e processados ​​são salvos em um arquivo CSV.

5-Compactação em ZIP : O arquivo CSV gerado é compactado no formato ZIP.

6-Limpeza de Arquivo CSV : Após a compactação, o arquivo CSV original é removido automaticamente.
