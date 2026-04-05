import pandas as pd
from fpdf import FPDF
import os

# Define o nome do arquivo CSV a ser lido (deve estar na mesma pasta do script)
nome_arquivo_csv = "DadosTeste.csv"

# Verifica se o arquivo existe antes de tentar ler
if not os.path.exists(nome_arquivo_csv):
    print(f"Não encontrei o arquivo '{nome_arquivo_csv}'")
    exit()

# Extrai o nome original do arquivo para usar no PDF
nome_base = os.path.splitext(nome_arquivo_csv)[0]
nome_pdf = f"Relatorio_{nome_base}.pdf"

# Lê os dados do CSV selecionado
df = pd.read_csv(nome_arquivo_csv)
total_familias = len(df)

# Trata o padrão brasileiro de casas decimais e converte para número
df['renda'] = df['renda'].astype(str).str.replace(',', '.')
df['renda'] = pd.to_numeric(df['renda'], errors='coerce')

# Estatísticas de Renda
n_renda = df['renda'].count() 
media_renda = df['renda'].mean()
min_renda = df['renda'].min()
max_renda = df['renda'].max()
q1_renda = df['renda'].quantile(0.25)
mediana_renda = df['renda'].quantile(0.50)
q3_renda = df['renda'].quantile(0.75)
q4_renda = df['renda'].quantile(1.00)

# Conta o uso do P.A.P removendo possíveis espaços em branco
df['p.a.p'] = df['p.a.p'].astype(str).str.strip() 
familias_usam_pap = df['p.a.p'].value_counts().get('usa', 0)

# Criamos uma classe personalizada para ter cabeçalho e rodapé
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Relatorio de Pesquisa', border=False, ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

# Inicializa o documento PDF
pdf = PDF()
pdf.add_page()

# Resumo Geral
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, txt="Resumo da Amostragem", ln=True)

pdf.set_font("Arial", size=12)
pdf.cell(0, 8, txt=f"Total de Familias Entrevistadas: {total_familias}", ln=True)
pdf.cell(0, 8, txt=f"Familias que usam o P.A.P: {familias_usam_pap}", ln=True)
pdf.ln(5)

# Bloco das Estatísticas de Renda
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 8, txt="Estatisticas da Renda (Salarios Minimos):", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 8, txt=f"  N (Valores validos): {n_renda}", ln=True)
pdf.cell(0, 8, txt=f"  Media: {media_renda:.2f}", ln=True)
pdf.cell(0, 8, txt=f"  Minimo: {min_renda:.2f}  |  Maximo: {max_renda:.2f}", ln=True)
pdf.cell(0, 8, txt=f"  Quartis: Q1 = {q1_renda:.2f}  |  Mediana = {mediana_renda:.2f}  |  Q3 = {q3_renda:.2f}  |  Q4 = {q4_renda:.2f}", ln=True)
pdf.ln(10)

# Tabela de Detalhamento
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, txt="Extrato dos Dados (Todas as familias)", ln=True)

# Cabeçalho da Tabela
pdf.set_font("Arial", 'B', 10)
pdf.cell(15, 10, 'Num', 1, align='C')
pdf.cell(45, 10, 'Local', 1, align='C')
pdf.cell(30, 10, 'P.A.P', 1, align='C')
pdf.cell(45, 10, 'Instrucao', 1, align='C')
pdf.cell(20, 10, 'Tam.', 1, align='C')
pdf.cell(25, 10, 'Renda', 1, align='C')
pdf.ln()

# Preenchendo a tabela com os dados
pdf.set_font("Arial", size=9)
for index, row in df.iterrows():
    pdf.cell(15, 8, str(row['núm.']), 1, align='C')
    
    local = str(row['local ']).strip()
    local = local[:17] + "..." if len(local) > 20 else local
    pdf.cell(45, 8, local, 1, align='C')
    
    pdf.cell(30, 8, str(row['p.a.p']), 1, align='C')
    pdf.cell(45, 8, str(row['instr.']), 1, align='C')
    pdf.cell(20, 8, str(row['tam.']), 1, align='C')
    
    renda_val = row['renda']
    renda_texto = "-" if pd.isna(renda_val) else f"{renda_val:.2f}"
    pdf.cell(25, 8, renda_texto, 1, align='C')
    
    pdf.ln()

# Guarda o arquivo
pdf.output(nome_pdf)
print(f"O arquivo '{nome_pdf}' foi criado.")