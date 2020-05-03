import argparse
import csv

from nota_carioca import recupera_imagem_nota_carioca, grava_imagem_nota


def carrega_notas_do_arquivo(arquivo):
    with open(arquivo, newline="") as csvfile:
        lista_notas = csv.DictReader(csvfile)
        return list(lista_notas)


def main(arquivo):
    lista_de_notas = carrega_notas_do_arquivo(arquivo)
    for nota in lista_de_notas:
        imagem = recupera_imagem_nota_carioca(**nota)
        grava_imagem_nota(imagem, **nota)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lê um arquivo CSV com a informação das notas a buscar.")
    parser.add_argument("arquivo", help="Arquivo .csv contendo o tipo, ccm(Inscrição Municipal), número da nota e código da nota")
    args = parser.parse_args()
    main(args.arquivo)
