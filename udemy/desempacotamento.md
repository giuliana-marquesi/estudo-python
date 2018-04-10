## Aula 8 da seção 1 - Desempacotamento ##

Esta aula foi muito interessante pois lembra de um conceito muito poderoso em python que é o desempacotamento.

É possível, a partir de uma sequência, listas ou strings por exemplo, colocar valores em variáveis separadas sem a necessidade de construir algo muito complexo. Apenas declarar uma sequencia de variaveis recebendo uma só sequencia.

		lista = [1,2,3,4]

		num1, _, num2, num3 = lista

		letras = 'abc'

		l1,l2,l3 = letras

É possível **pular** um item da sequÊncia usando o **_** no lugar de uma variável

Um porém é a necessidade de declarar ou usar underscore para o numero exato de itens da sequência.

No retorno de uma função com mais de um valor o que ocorre, na verdade, é o retorno de uma tupla (qualquer variavel que possui dois ou mais elementos entre virgulas se torna uma tupla com estes valores), logo também poderá ser desempacotado.

```
		def funcao(x,y):
			return x**2, y**2

		r1,r2 = funcao(2,3)

```
