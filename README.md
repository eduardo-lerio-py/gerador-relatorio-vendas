# Gerador de Relatório de Vendas

Programa em Python que lê um arquivo CSV de vendas, calcula os principais números e gera um relatório em texto.

## Requisitos

Python 3.6 ou superior. Não precisa instalar nenhuma biblioteca.

## Como rodar

```
python gerador_relatorio_vendas.py
```

O programa pergunta o nome do arquivo CSV. Para usar o de exemplo, é só apertar Enter.

## Formato do CSV

Colunas obrigatórias: `produto`, `categoria`, `quantidade` e `valor`.

## O que o relatório mostra

- Total vendido e número de vendas
- Unidades vendidas e ticket médio
- Produto mais vendido
- Total por categoria

## Exemplo

```
Nome do arquivo CSV (Enter para vendas.csv): 
Preço total: 1230.70
Número total de vendas: 10
Número total de produtos vendidos: 23
Ticket médio: 123.07
Produto mais vendido: Meia
Roupas: 361.80
Casa: 269.20
Calçados: 599.70
Relatório gerado com sucesso!
```

## Arquivos com problemas

- Aceita vírgula decimal (`49,90`)
- Ignora linhas com campos vazios ou inválidos e avisa quais foram (teste com `vendas_sujas.csv`)
- Avisa se o arquivo não existe ou se faltam colunas
