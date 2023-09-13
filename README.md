<h1 align="center">Conway </h1>
<p align="center">
Jogo do Conway feito em Python
</p>
<p align="center" >
<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=RED&style=for-the-badge"/>
</p>

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Regras](#regras)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)


## Descrição do projeto

O "Jogo da Vida de Conway" (Conway's Game of Life) não é um jogo no sentido tradicional, mas sim um autômato celular inventado pelo matemático britânico John Horton Conway em 1970. É um modelo de simulação que opera em uma grade bidimensional infinita (ou limitada) de células quadradas, cada uma podendo estar em um de dois estados: vivo ou morto (ou ativo ou inativo). O jogo segue algumas regras simples que determinam o estado futuro das células com base no estado atual delas e no estado das células vizinhas.

## Regras

As regras do Jogo da Vida de Conway:

1. **Nascimento:** Se uma célula morta (inativa) tiver exatamente 3 células vizinhas vivas (ativas), ela se tornará viva na próxima geração.

2. **Sobrevivência:** Se uma célula viva (ativa) tiver 2 ou 3 células vizinhas vivas, ela permanecerá viva na próxima geração.

3. **Morte:** Se uma célula viva tiver menos de 2 células vizinhas vivas (solidão) ou mais de 3 células vizinhas vivas (superpopulação), ela morrerá (ficará inativa) na próxima geração.

O jogo começa com um estado inicial, que é chamado de "geração 0". A partir desse estado inicial, as regras do jogo são aplicadas iterativamente para gerar novas gerações. Cada nova geração é calculada com base na geração anterior.

O Jogo da Vida de Conway é fascinante por várias razões:

1. **Complexidade Emergente:** Mesmo que as regras sejam simples, o jogo pode gerar padrões complexos, como blocos osciladores, espaçonaves, padrões estáveis e caóticos. Alguns padrões são estáveis e não mudam, enquanto outros continuam a evoluir indefinidamente.

2. **Universalidade:** O Jogo da Vida de Conway é Turing completo, o que significa que pode ser usado para simular qualquer máquina de Turing, o que torna possível implementar cálculos e lógica computacional nele.

3. **Aplicações:** Embora originalmente concebido como uma experiência matemática, o Jogo da Vida de Conway também encontrou aplicações em várias áreas, como pesquisa de algoritmos, simulações científicas e até mesmo em arte computacional.

O Jogo da Vida de Conway não envolve jogadores ou estratégia, mas é um exemplo interessante de como regras simples podem levar a comportamentos complexos e imprevisíveis em sistemas dinâmicos. É frequentemente explorado como um desafio de programação e também é usado como uma metáfora em muitos campos da ciência e da computação para ilustrar princípios de complexidade e sistemas dinâmicos.

## Pré requisitos

Ter o python instalado em sua máquina. No meu projeto foi usado o python3

## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/Henrique088/Programacao-orientada-a-objeto-em-python.git
```

Depois abra o terminal dentro da pasta do arquivo e digite o comando: 

```
python3 main.py

```

