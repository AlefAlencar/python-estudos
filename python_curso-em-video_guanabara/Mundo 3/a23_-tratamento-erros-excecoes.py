# TRATAMENTO DE ERROS E EXCEÇÕES

# try:
#   operação
# except:       <-pode ter vários exceções específicos
#   falhou
# else:     <-opcional
#   deu certo
# finally:  <-opcional
#   certo/falha

try:        # TENTE OPERAÇÃO
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário não informou os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:       # DEU CERTO (opcional)
    print(f'O resultado é {r:.2f}')
finally:    # CERTO ou FALHA (opcional)
    print('Volte sempre! Muito obrigado!')
