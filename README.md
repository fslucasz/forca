# Jogo da Forca em Python

## Integrantes da Equipe

* Lucas Floriano de Sousa
* Lucas Montagnoli

## Tema Escolhido

**Jogos de Adivinhação / Lógica de Programação**

O tema aborda o clássico jogo da forca, implementado via linha de comando (terminal) de forma interativa e educativa.

## Objetivo do Sistema

O objetivo do sistema é proporcionar uma experiência simples e divertida do jogo da forca, permitindo que o usuário exercite o raciocínio lógico e vocabulário relacionado à tecnologia/programação. Além disso, o projeto visa demonstrar conceitos fundamentais da linguagem Python, como:

* Estruturas de repetição (`while`, `for`)

* Condicionais (`if`, `else`)

* Manipulação de strings e listas

* Uso de módulos nativos (`random`)

## Breve Descrição do Funcionamento

1. **Sorteio da Palavra:** O programa seleciona aleatoriamente uma palavra de uma lista pré-definida de termos de tecnologia (`python`, `programacao`, `computador`, `dados`, `desenvolvimento`).

2. **Interface Visual:** Exibe a palavra oculta usando traços (`_`) para cada letra não descoberta.

3. **Entrada do Jogador:** O usuário digita uma letra por tentativa.

4. **Validações:**

   * O sistema verifica se a letra já foi digitada anteriormente para evitar desperdício de tentativas.

   * Se a letra pertencer à palavra, ela é revelada nas posições corretas.

   * Se a letra não pertencer, o jogador perde 1 tentativa (limite máximo de **6 erros**).

5. **Condição de Vitória/Derrota:**

   * **Vitória:** Todas as letras são descobertas antes de atingir o limite de erros.

   * **Derrota:** O número de erros atinge o limite máximo de 6 e a palavra correta é revelada.

## Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.

2. Baixe ou clone este repositório.
   ´´´
  git clone https://github.com/fslucasz/forca.git
  
```

4. Abra o terminal/prompt no diretório do projeto.

5. Execute o seguinte comando:
´´´
python forca.py

```
