# Projeto: Análise e Propostas de Títulos para Plataformas de Streaming

## Objetivo da Atividade
Este projeto tem como objetivo **analisar os catálogos de títulos das plataformas Netflix, Disney+ e Amazon Prime Video** (fornecidos em arquivos CSV) e, a partir dessas análises, **propor novos filmes e séries com alta probabilidade de sucesso**, conforme solicitado na atividade da disciplina de Data Science / Estatística.  
O projeto foi dividido em **duas partes complementares**:
1. **Análise de Dados (Python):** exploração e resumo dos catálogos existentes.  
2. **Criação de Propostas (Manual):** interpretação dos dados e elaboração de novos títulos com justificativas.

---

## Estrutura do Projeto
```
StreamingAnalysis/
│
├── data/                         # Arquivos originais fornecidos
│   ├── netflix_titles.csv
│   ├── disney_plus_titles.csv
│   └── amazon_prime_titles.csv
│
├── analysis/
│   └── analyze_streaming.py       # Script Python que realiza a análise dos dados
│
├── output/                        # Resultados gerados automaticamente
│   ├── summary_report.csv         # Relatório técnico com estatísticas por plataforma
│   └── summary_report.md          # Relatório em formato Markdown
│
├── propostas.md                   # Documento com as propostas criativas (filmes e séries)
└── README.md                      # Este arquivo
```

---

## Parte 1 — Análise de Dados
O script `analyze_streaming.py` é responsável por:
- Ler os três arquivos CSV fornecidos (`netflix_titles.csv`, `disney_plus_titles.csv`, `amazon_prime_titles.csv`);
- Limpar e padronizar os dados;
- Calcular as seguintes métricas principais:
  - Gêneros mais frequentes (`listed_in`);
  - Distribuição de anos de lançamento (`release_year`);
  - Classificações indicativas mais comuns (`rating`);
  - Países predominantes (`country`);
  - Duração média dos títulos (`duration`);
- Gerar automaticamente os arquivos de saída:
  - `summary_report.csv` — relatório detalhado com estatísticas;
  - `summary_report.md` — versão legível das análises para inserção no relatório final.

---

## Parte 2 — Criação de Títulos
O documento `propostas.md` contém **um filme e uma série propostos para cada plataforma**, incluindo:
- Nome do título;
- Gênero;
- Sinopse curta;
- Público-alvo (rating);
- Porcentagem estimada de sucesso (`sucesso`);
- Justificativa baseada nos dados obtidos na análise.

Essas propostas foram desenvolvidas **manualmente com base nas tendências identificadas** pela análise de dados do script Python.

---

## Como Executar o Projeto

### 1. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate   # (Windows)
```

### 2. Instalar dependências
```bash
pip install pandas
```

### 3. Executar o script de análise
```bash
python analysis/analyze_streaming.py
```

Os arquivos de resultado serão gerados automaticamente dentro da pasta `output/`.

---

## Entregáveis da Atividade
| Item | Descrição | Local |
|------|------------|-------|
| **Análise de Dados** | Código Python com tratamento e estatísticas | `analysis/analyze_streaming.py` |
| **Relatório de Saída (CSV/MD)** | Resultados da análise de dados | `output/summary_report.*` |
| **Propostas Criativas** | 3 filmes e 3 séries com justificativas | `propostas.md` |
| **Documentação Geral** | Explicação e estrutura do projeto | `README.md` |

---

## 👩‍💻 Autoria
Projeto desenvolvido por **Giullia Ortiz Vilanova**, no contexto da disciplina de **Projeto de Mineração de Dados**, com o objetivo de conectar análise estatística e criatividade para previsão de sucesso no mercado de streaming.
