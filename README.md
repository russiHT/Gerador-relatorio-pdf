# Gerador de Relatório Estatístico em PDF

*[Read this in English below](#english-version)*

**Gerador de Relatório Estatístico** é um script em Python desenvolvido para automatizar a leitura, limpeza e análise de bases de dados. O sistema permite a ingestão de planilhas CSV, calcula medidas estatísticas e gera automaticamente um relatório completo e formatado em PDF.

## Tecnologias
- **Python 3**
- **Pandas** (Tratamento de dados e cálculos estatísticos)
- **FPDF** (Geração e formatação de documentos PDF)
- **OS** (Navegação de diretórios nativa do Python)

## Funcionalidades
- **Ingestão de Dados:** Leitura automática de arquivos `.csv`.
- **Data Cleaning (Limpeza de Dados):** Tratamento do padrão brasileiro de casas decimais (conversão de vírgulas para pontos) e de valores nulos/ausentes.
- **Análise Estatística:** Cálculo automático do total de amostras válidas, média, mínimo, máximo e quartis (Q1, Mediana e Q3).
- **Geração de PDF:** Criação dinâmica de um documento com múltiplas páginas, contendo cabeçalho, paginação automática, resumo estatístico e tabela detalhada.

## Como rodar
1. Clone o repositório:
   ```bash
   git clone https://github.com/russiHT/Gerador-relatorio-pdf.git
   ```
   
2. Certifique-se de ter o Python 3 instalado e instale as dependências:
   ```bash
   pip install pandas fpdf
   ```
   
3. Coloque o arquivo de dados na raiz do projeto com o nome `DadosTeste.csv`.

4. Execute a aplicação via terminal:
   ```bash
   python GeradorRel.py
   ```
   
5. O arquivo `Relatorio_DadosTeste.pdf` será gerado automaticamente na mesma pasta.

# English Version

**Statistical PDF Report Generator** is a Python script developed to automate the reading, cleaning, and analysis of datasets. The system allows the ingestion of CSV spreadsheets, calculates statistical measures, and automatically generates a comprehensive, formatted PDF report.

## Technologies
- **Python 3**
- **Pandas** (Data manipulation and statistical calculations)
- **FPDF** (PDF document generation and formatting)
- **OS** (Python native directory navigation)

## Features
- **Data Ingestion:** Automated reading of `.csv` files.
- **Data Cleaning:** Handling of the Brazilian decimal standard (converting commas to dots) and missing/null values.
- **Statistical Analysis:** Automatic calculation of total valid samples, mean, minimum, maximum, and quartiles (Q1, Median, and Q3).
- **PDF Generation:** Dynamic creation of a multi-page document featuring a header, automatic pagination, statistical summary, and detailed data table.

## How to run
1. Clone the repository:
   ```bash
   git clone https://github.com/russiHT/Gerador-relatorio-pdf.git
   ```
2. Make sure you have Python 3 installed, then install the dependencies:
   ```bash
   pip install pandas fpdf
   ```
   
3. Place the data file in the root directory.

4. Run the application via terminal:
   ```bash
   python GeradorRel.py
   ```
   
5. The file `Relatorio_DadosTeste.pdf` will be automatically generated in the same folder.

## Autor / Author
Gustavo Iensue Russi

Estudante de Engenharia de Computação na UEPG | Computer Engineering Student at UEPG
