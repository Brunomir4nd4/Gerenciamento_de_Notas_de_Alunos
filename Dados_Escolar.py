# git checkhot -b main
import ast
import statistics
#notas = {"LUIS": [9.0, 8.0], "MATHEUS": [7.5, 9.0], "BRUNO": [10.0, 8.5], "LEIZIANE": [10.0, 10.0]}


se = 1
pesoProva = 2
add = "1 Adicionar aluno"
most = "2 Mostrar notas dos alunos"
se = "3 Semestres"
med = "4 média dos alunos"
delet = "5 Deletar anluno"
sair = "0 Sair"
#----------------------------------------------------------#
def novoAluno(nome):    
        l = []
        cont = 1
        for i in range(qtdnotas):
            l.append(float(input(f"Digite a {cont}º nota "))) 
            cont += 1
        notas[nome] = l
        print("Aluno adicionado com sucesso!")


arquivo = open("dicionario.txt", "r")
notas = ast.literal_eval(arquivo.read())
arquivo.close()

    
while 1:
    print("#"*33)
    print('#' + add.center(31) + '#')
    print('#' + most.center(31) + '#')
    print('#' + se.center(31) + '#')
    print('#' + med.center(31) + '#')
    print('#' + delet.center(31) + '#')
    print('#' + sair.center(31) + '#')
    print("#"*33)
    swtchi = int(input())
    
    if swtchi == 1:
        nome = input("Nome do novo Aluno: ")
        nome = nome.upper()
        if nome in notas:
            m = input("Esta chave já existe, gotaria de atualizar as notas? (s) ou (n) ")
            if m == 's':
                qtdnotas = int(input("Digite a quatidade de provas: "))
                novoAluno(nome)
        else:   
            qtdnotas = int(input("Digite a quantidade de provas: "))
            novoAluno(nome)
    
    elif swtchi == 2:
        print("1º Nota global")
        print("2º Notas individuais")
        subMost = int(input())
        
        if subMost == 1:
            l = list(notas)
            for i in range(len(l)):
                print(l[i])
                print(notas[l[i]])
                i += 1
        else:
            nome = input("Nome do novo Aluno: ")
            nome = nome.upper()
            if nome in notas:
                print(f'As notas do/a aluno/a {nome} são: {notas[nome]}')
            else:
                m = input("Esta chave não existe, gostária de adiciona-lá? (s) ou (n) ")
                if m == "s":
                    qtdnotas = int(input("Digite a quantidade de provas: "))
                    novoAluno(nome)

    elif swtchi == 3:
        m = input(f"Semestre atual é {se} gostária de trocar? (s) ou (n) ")
        if m == 's':
            se = int(input("Digite o Semestre: "))
            pesoProva = 2 * se
            print("Semestre alterado com sucesso!")
        else:
            print("Semestre não alterado")
    
    elif swtchi == 4:
        print("1º Média global")
        print("2º Médias individuais")
        subMed = int(input())
        
        if subMed == 1:
            l = list(notas)
            
            for i in range(len(l)):
                media = statistics.mean(notas[l[i]])
                print(l[i])
                print(media)
                i += 1
        else:
            nome = input("Nome do Aluno: ")
            nome = nome.upper()
            media = statistics.mean(notas[nome])
            print(f"A média do aluno {nome} é: {media}")
    
    elif swtchi == 5:
        nome = input("Nome do Aluno: ")
        nome = nome.upper()
        m = input(f"Todos os dados de {nome} serão deletados! Proceguir (s) ou (n) ")
        if m == 's':
            del notas[nome]
            print("Dados deletados")
    else:
        print("Programa finalizado")
        arquivo = open("dicionario.txt", "w")
        notas = str(notas)
        notas = arquivo.write(notas)
        arquivo.close()
        break