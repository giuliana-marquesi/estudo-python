##Estudo sobre aula 16 da seção 1, Threads ##

O professor falou muito por cima sobre o uso do módulo (classe) Thread já implementada em Python. Gostaria de saber mais sobre seu uso e como funciona.

### O módulo threading ###

Ao pesquisar sobre quais são os outros métodos implementados na classe Thread descobri na documentação do Python outro módulo chamado *threading*. Então, soube que em Python3, não sei que versão exatamente, este é o módulo aconselhado a ser chamado para quando se quer usar threads. É uma interface com maior alto nível de abstração para o módulo \_thread.

Não pratiquei nenhum dos dois métodos para sentir suas diferenças e vatagens. A princípio, o módulo threading possuí alguns métodos a mais de controle de thread.

Para usá-lo é possível instanciá-lo diretamente:

		import threading

		t = threading.Thread(target=funcao(), args=(argumentos), name='T-2')

Ou é possível criar uma classe que herda Thread:

		from threading import Thread

		class Worker(Thread):
			pass

### O uso de paralelismo e outras formas ###

Não possuo conhecimento muito amplo de quando se deve escolher entre as diferentes possíbilidades de não se prender um código a uma resposta síncrona. Existem diferentes abordagens como o multiprocessamento, thread, assincronicidade.

Para deixar anotado um método que me chamou atenção e pretendo usar como estudo, talvez, no TG é o **asyncio**.
