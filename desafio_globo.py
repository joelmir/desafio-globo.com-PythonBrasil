

def frequencia(string_qualquer):
  '''
  Inspeciona uma string qualquer
  e retorna um dicionario com cada string e a quantidade da ocorrencia
  dela

  teste simples
  >>> frequencia('teste')
  {'s': 1, 'e': 2, 't': 2}

  teste com string vazia
  >>> frequencia('')
  {}

  teste com ocorrencia de caracteres maiúsculo e minúsculo
  >>> frequencia('tEsTe')
  {'s': 1, 'e': 2, 't': 2}
  '''
  dicionario = {}
  for c in string_qualquer:
    chave = c.lower()
    if chave in dicionario:
      dicionario[chave] += 1
    else:
      dicionario[chave] = 1
  return dicionario


if __name__ == '__main__':
  import doctest
  print doctest.testmod()
  print frequencia('blabla')
