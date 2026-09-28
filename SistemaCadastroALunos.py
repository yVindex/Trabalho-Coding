alunos = []

def menu_sistema_cadastro():
    print("-----------SISTEMA DE CADASTRO DE ALUNOS-----------")
    print("1. Adicionar aluno ")
    print("2. Listar todos os alunos ")
    print("3. Buscar aluno pelo nome ")
    print("4. Remover aluno ")
    print("5. Mostrar média geral das notas ")
    print("6. Sair ")
    print("---------------------------------------------------")

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    while True:
        idade = input("Digite a idade do aluno: ")

        if idade.isdigit():
         idade = int(idade)
        else:
            print("A idade deve ser um NUMERO.")
            continue

        if idade > 0:
            break
        else:
            print("A idade deve ser maior que 0.")

    while True:
        nota = input("Digite a nota do aluno: ")

        if nota.isdigit():
            nota = int(nota)
        else:
            print("A nota deve ser um NUMERO.")
            continue

        if 0 <= nota <= 10:
            break
        else:
             print("A nota deve estar entre 0 e 10.")


    aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }
    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")



def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    print("-----------Lista de Alunos-----------")
    for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']} anos")
            print(f"Nota: {aluno['nota']:.1f}")
            print("------------------------")


def buscar_aluno():
    nome_buscar = input("Digite o nome do aluno que deseja buscar: ")

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_buscar.lower():
            print("\nAluno encontrado!")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']} anos")
            print(f"Nota: {aluno['nota']:.1f}")

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")


def remover_aluno():
    nome_remover = input("Digite o nome do aluno que deseja remover: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome_remover.lower():
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return

    print("Aluno não encontrado.")