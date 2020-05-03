import requests

URL_IMAGEM_NOTA_CARIOCA = "https://notacarioca.rio.gov.br/contribuinte/notaprintimg.aspx"


def recupera_imagem_nota_carioca(**kwargs):
    resp = requests.get(URL_IMAGEM_NOTA_CARIOCA,
                        params={"ccm": kwargs["ccm"], "nf": kwargs["nf"], "cod": kwargs["cod"], "imprimir": 0})
    return resp.content


def grava_imagem_nota(image_data, **kwargs):
    with open(f"{kwargs['tipo']}_{kwargs['nf']}_{kwargs['cod']}.gif", "wb") as image_file:
        image_file.write(image_data)
