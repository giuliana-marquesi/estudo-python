## Aula Programação funcional ( Seção 1 Aula 5) ##

O que teve de mais relevante foi a função *lambda* e o uso de algumas funções como auxiliares como o
*map*, *filter*.

### Pesquisa sobre função *lambda* ###
 
 É uma função que não precisa ser declarada, anônima. Executa tarefas simples que cabem em uma linha. Por isso o uso frequente no paradigma funcional onde deve-se dar o minimo de responsabilidade possível à uma função.

 ### Sobre *map* ###

		map(function, iterable,...)

Ele itera aplicando uma função. Esta função acima é o modo de uso mais básico, que retorna o resultado da ação da função iterando, logo, cria um **OBJETO** iterável.

### Sobre *filter* ###

Como o nome diz, esta função **filtra** um determinado tipo de elemento dentro de uma lista (sequencia iterável). Para filtrar é preciso passar uma função que determina o que será aceito ou não nesta nova sequencia.
### PS ###

* Com o *lambda* o uso destas função fica mais direto, não necessitando de uma declaração mais verbosa para algo mais simples.

* Importante: para que o objeto iterável consiga ser usado em funçãoes de listas é preciso fazer um casting:

		list(map(lambda x: x**2, [1,2,3]))
