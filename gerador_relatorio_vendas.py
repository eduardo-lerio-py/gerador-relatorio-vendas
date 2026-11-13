import csv
COLUNAS = {"produto", "categoria", "quantidade", "valor"}


def ler_vendas(caminho):
    vendas = []
    ignoradas = []

    with open(caminho, encoding="utf-8-sig", newline="") as f:
        primeira = f.readline()
        delimitador = ";" if ";" in primeira else ","
        f.seek(0)
        leitor = csv.DictReader(f, delimiter=delimitador)

        faltando = COLUNAS - set(leitor.fieldnames or [])
        if faltando:
            raise ValueError(f"Colunas faltando no arquivo: {', '.join(sorted(faltando))}")

        for numero, linha in enumerate(leitor, start=2):
            try:
                quantidade = int(linha["quantidade"])
                valor = float(linha["valor"].replace(",", "."))
            except (ValueError, TypeError, AttributeError):
                ignoradas.append(f"linha {numero}: quantidade ou valor inválido")
                continue
            vendas.append({
                "produto": linha["produto"],
                "categoria": linha["categoria"],
                "quantidade": quantidade,
                "valor": valor,
            })

    return vendas, ignoradas


def calcular_resumo(vendas):

    unidades = 0
    total = 0
    por_categoria = {}
    qtd_por_produto = {}

    for v in vendas:
        total_linha = v["quantidade"] * v["valor"]
        total += total_linha
        unidades += v["quantidade"]
        categoria = v["categoria"]
        produto = v["produto"]
        por_categoria[categoria] = por_categoria.get(categoria, 0) + total_linha
        qtd_por_produto[produto] = qtd_por_produto.get(produto, 0) + v["quantidade"]

    num_de_vendas = len(vendas)

    ticket_medio = 0
    if num_de_vendas > 0:
        ticket_medio = total / num_de_vendas

    mais_vendido = None
    if qtd_por_produto:
        mais_vendido = max(qtd_por_produto, key=qtd_por_produto.get)

    return {
        "total": total,
        "num_de_vendas": num_de_vendas,
        "unidades": unidades,
        "ticket_medio": ticket_medio,
        "por_categoria": por_categoria,
        "mais_vendido": mais_vendido,
    }


def mostrar_resumo(resumo):
    print(f"Preço total: {resumo['total']:.2f}")
    print(f"Número total de vendas: {resumo['num_de_vendas']}")
    print(f"Número total de produtos vendidos: {resumo['unidades']}")
    print(f"Ticket médio: {resumo['ticket_medio']:.2f}")
    print(f"Produto mais vendido: {resumo['mais_vendido']}")
    for categoria, total in resumo["por_categoria"].items():
        print(f"{categoria}: {total:.2f}")


def exportar_txt(resumo, caminho):
    with open(caminho, "w", encoding="utf-8") as r:
        print("RELATÓRIO DE VENDAS", file=r)
        print("-" * 30, file=r)
        print(f"Total vendido: R$ {resumo['total']:.2f}", file=r)
        print(f"Número de vendas: {resumo['num_de_vendas']}", file=r)
        print(f"Ticket médio: R$ {resumo['ticket_medio']:.2f}", file=r)
        print(f"Produto mais vendido: {resumo['mais_vendido']}", file=r)
        print("\nPor categoria:", file=r)
        for categoria, total in resumo["por_categoria"].items():
            print(f"  {categoria}: {total:.2f}", file=r)


def main():
    caminho = input("Nome do arquivo CSV (Enter para vendas.csv): ").strip() or "vendas.csv"

    try:
        vendas, ignoradas = ler_vendas(caminho)
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
        return
    except ValueError as erro:
        print(erro)
        return

    for aviso in ignoradas:
        print(f"Ignorada: {aviso}")

    if not vendas:
        print("Nenhuma venda válida encontrada.")
        return

    resumo = calcular_resumo(vendas)
    mostrar_resumo(resumo)
    exportar_txt(resumo, "relatorio.txt")
    print("Relatório gerado com sucesso!")


if __name__ == "__main__":
    main()
