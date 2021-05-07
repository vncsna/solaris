# Desafio Técnico - Engenheiro de Software 1

## Intruções
Na raiz deste repositório existe um dataset (people_data.csv) com dados cadastrais
de algumas pessoas. **Estes dados são fictícios e foram gerados no site [4devs.com.br](https://www.4devs.com.br)**.

O desafio consiste em desenvolver uma aplicação web, (Preferencialmente em python) que exponha informações
deste dataset nas seguintes rotas:
- **/youngers/{n}**: Retorna uma lista das n pessoas mais jovens ordenadas ascendentemente
- **/olders/{n}**: Retorna uma lista das n pessoas mais velhas ordenadas ascendentemente
- **/gender-distribution**: Retorna um Json com a distribuição percentual de generos no dataset: Ex.: {"Feminino" 51%, "Masculino": 49%}
- **/people/{cpf_without_punctuation}**: Retorna os dados de uma única pessoa em formato json
- **/blood-type/stats**: retorna a distribuição absoluta de grupos sanguíneos: {"B-": 20, "O+": 10...}
- **/peoples**: Listar os nomes de todas as pessoas no dataset em ordem alfabética
- **/peoples/search?q=query**: Busca pessoas por nome ou por parte do nome (case insensitive)

## Tecnologias
Você é livre para usar quaisquer frameworks que julgar necessário para resolver o problema proposto.
Também poderá persistir os dados da forma que julgar mais conveniente.

Enfim, você é livre para escolher as tecnologias que vai usar neste desafio, mas esteja preparado(a) para justificar suas escolhas.

Encapsular sua solução em uma imagem docker não é mandatório mas será considerado um plus.

Boa Sorte!
