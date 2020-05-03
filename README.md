# Baixador de Imagens de Nota Carioca

Este programa serve para baixar as imagens das notas pariocas para facilitar os pedidos de reembolso de certas operadoras de planos de saúde.

## Uso

É preciso instalar a única dependência através de `pip install requests`

É preciso ter um arquivo .csv no seguinte formato:

```
tipo,ccm,nf,cod
<TIPO>,<Inscrição Municipal>,<Número da nota fiscal>,<Código da nota fiscal>
```

A invocação do programa se dá da segunte forma:
`python baixa_notas.py <arquivo de notas>.csv`

O programa baixará para o diretório atual todos as imagens das notas fiscais e os salvará com os seguintes nomes de arquivo:

`<Tipo>_<Número da nota fiscal>_<Código da nota fiscal>.gif`

## Biblioteca

As funções de recuperação e gravação dos dados da nota estão segregados no próprio módulo, portanto basta importá-los no seu projeto para usar.

```python
from nota_carioca import recupera_imagem_nota_carioca, grava_imagem_nota
```

## TO-DO

Remover a dependência de `Requests`