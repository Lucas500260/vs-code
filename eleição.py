candidato_X = 0
candidato_Y = 0
candidato_Z = 0
branco = 0
eleicao = False
eleitores = int(input("informe o número de eleitores: "))
print ('Candidato X vote no número 889''\nCandidato Y vote no número 847''\nCandidato Z vote no número 515''\nPara votar em Branco digite 0')
while eleicao == False:
    condicao = False
    while eleicao == False:
     for i in range(eleitores):
      voto = input("Digite o número do Candidato que quer votar "
        f"\neleitor {i + 1} quer votar: " )
      if voto == "889":
        candidato_X += 1
        eleicao = True
      elif voto == "847":
        candidato_Y += 1
        eleicao = True
      elif voto == "515":
        candidato_Z += 1
        eleicao = True
      elif voto == "0":
        branco +=1
        eleicao = True
      else:
        print('voto Inválido')
    while condicao == False:
        try:
            print('\nDeseja finalizar a eleição?''\n1 - sim''\n2 - não')
            opcao = int(input('\nOpção: '))
            if opcao == 1:
                eleicao =  True
                condicao = True
            elif opcao == 2:
                eleicao = False
                condicao = True
            else:
                print('\nEscolha apenas as opções 1 e 2.')
        except:
            print('\nEscolha apenas as opções 1 e 2.')
if candidato_X > candidato_Y and candidato_X > candidato_Z:
    candidato = 'Candidat X'
elif candidato_Y > candidato_X and candidato_Y > candidato_Z:
    candidato = 'Candidato y'
elif candidato_Z > candidato_X and candidato_Z > candidato_Y:
    candidato = 'Candidato Z'
else:
    candidato = 'Empate'
print(
    "Votação encerrada"
    f"\nCandidato X: {candidato_X} voto(s)"
    f"\nCandidato Y {candidato_Y} voto(s)"
    f"\nCandidato Z: {candidato_Z} voto(s)"
    f"\nVotos em Branco: {branco} votos(s)"
)
if candidato == 'Empate':
    print('Aconteceu um empate...')
else:
    print(f'\nO vencedor foi o {candidato}.')