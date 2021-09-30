#!/usr/bin/env python3
# modelo06.py

# Esse exemplo mostra o funcionamento de ATRIBUTOS DE CLASSE COM TIPOS IMUTÁVEIS.

class ObjetoContavel:
    contador = 0
    limite = 3


class ComentarioContavel(ObjetoContavel):
    def __init__(self, comentario):
        if self.contador >= self.limite:
            raise Exception
        else:
            self.__class__.contador += 1
        self.comentario = comentario


class PostagemContavel(ObjetoContavel):
    def __init__(self, postagem):
        if self.contador >= self.limite:
            raise Exception
        else:
            self.__class__.contador += 1
        self.postagem = postagem


post_1 = PostagemContavel('Eu acho python muito legal!')
coment_1 = ComentarioContavel('Concordo com a sua opinião.')
print('-> post1 e coment1 criados')
print('c pai.cont', ObjetoContavel.contador)  # 0
print('c post.cont', PostagemContavel.contador)  # 1
print('c coment.cont', ComentarioContavel.contador)  # 1
print('post1.cont', post_1.contador)  # 1
print('coment1.cont', coment_1.contador, '\n')  # 1

print('c pai.lim', ObjetoContavel.limite)  # 3
print('c post.lim', PostagemContavel.limite)  # 3
print('c coment.lim', ComentarioContavel.limite)  # 3
print('post1.lim', post_1.limite)  # 3
print('coment1.lim', coment_1.limite, '\n')  # 3

post_2 = PostagemContavel('Python é massa!')  # <-- mexe no contador de todas as instâncias criadas e da classe,
# ## mas não no da superclasse PAI (ObjetoContavel)
print('-> post2 criado')
print('c pai.cont', ObjetoContavel.contador)  # 0
print('c post.cont', PostagemContavel.contador)  # 2
print('c coment.cont', ComentarioContavel.contador)  # 1
print('post1.cont', post_1.contador)  # 2
print('post2.cont', post_2.contador)  # 2
print('coment1.cont', coment_1.contador, '\n')  # 1

print('c pai.lim', ObjetoContavel.limite)  # 3
print('c post.lim', PostagemContavel.limite)  # 3
print('c coment.lim', ComentarioContavel.limite)  # 3
print('post1.lim', post_1.limite)  # 3
print('post2.lim', post_2.limite)  # 3
print('coment1.lim', coment_1.limite, '\n')  # 3

post_1.limite = 5
coment_1.limite = 7  # <-- a var 'limite' só é alterada na instância específica,
# ## pois não foi inicializada como self.__class__.xxxxxx
print('-> post1 limite = 5')
print('c pai.lim', ObjetoContavel.limite)  # 3
print('c post.lim', PostagemContavel.limite)  # 3
print('c coment.lim', ComentarioContavel.limite)  # 3
print('post1.lim', post_1.limite)  # 5
print('post2.lim', post_2.limite)  # 3
print('coment1.lim', coment_1.limite, '\n')

coment_2 = ComentarioContavel('Só, pode crer.')
coment_3 = ComentarioContavel('Certeza mano.')
print('-> coment 2 e 3 criados')
print('c pai.cont', ObjetoContavel.contador)  #
print('c post.cont', PostagemContavel.contador)  #
print('c coment.cont', ComentarioContavel.contador)  # 3
print('post1.cont', post_1.contador)  # 2
print('post2.cont', post_2.contador)  # 2
print('coment1.cont', coment_1.contador)  # 3
print('coment2.cont', coment_2.contador)  # 3
print('coment3.cont', coment_3.contador, '\n')  # 3
# Descomentar para ver a exceção. Comentar para executar
# os comandos abaixo. A exceção interrompe o programa.
# comentario_extra = ComentarioContavel('Tambem acho.')
# Traceback (most recent call last):
# ...
# Exception
ObjetoContavel.limite = 10  # <-- alterar a variável da classe-pai altera em cascata as classes-filhas e as
# ## instâncias criadas a partir destas classes, EXCETO para as variáveis alteradas duma instância específica
print('-> C PAI limite = 10')
print('c pai.lim', ObjetoContavel.limite)  # 10
print('c post.lim', PostagemContavel.limite)  # 10
print('c coment.lim', ComentarioContavel.limite)  # 10
print('post1.lim', post_1.limite)  # 5
print('post2.lim', post_2.limite)  # 10
print('coment1.lim', coment_1.limite)  # 10
print('coment2.lim', coment_2.limite)  # 10
print('coment3.lim', coment_3.limite, '\n')  # 10

coment_4 = ComentarioContavel('Tambem acho.')
print('-> coment4 criado')
print('c pai.cont', ObjetoContavel.contador)  # 0
print('c post.cont', PostagemContavel.contador)  # 2
print('c coment.cont', ComentarioContavel.contador)  # 4
print('post1.cont', post_1.contador)  # 2
print('post2.cont', post_2.contador)  # 2
print('coment1.cont', coment_1.contador)  # 4
print('coment2.cont', coment_2.contador)  # 4
print('coment3.cont', coment_3.contador)  # 4
print('coment4.cont', coment_4.contador, '\n')  # 4
