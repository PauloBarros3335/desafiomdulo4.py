students = []



def menu():

    print("\nMenu de Opções")

    print("1. Adicionar Estudante")

    print("2. Listar Estudantes")

    print("3. Buscar Estudante")

    print("4. Editar Estudante")

    print("5. Remover Estudante")

    print("6. Sair")



def add_student():

    name = input("Digite o nome do estudante: ")

    if any(student['name'] == name for student in students):

        print("Estudante já cadastrado.")

    else:

        age = input("Digite a idade do estudante: ")

        city = input("Digite a cidade onde o estudante vive: ")

        students.append({"name": name, "age": age, "city": city})

        print(f"Estudante {name} adicionado com sucesso.")



def list_students():

    if students:

        print("\nLista de Estudantes:")

        for student in sorted(students, key=lambda s: s['name']):

            print(f"Nome: {student['name']}, Idade: {student['age']}, Cidade: {student['city']}")

    else:

        print("Nenhum estudante cadastrado.")



def search_student():

    name = input("Digite o nome do estudante que deseja buscar: ")

    for student in students:

        if student['name'] == name:

            print(f"Estudante encontrado: Nome: {student['name']}, Idade: {student['age']}, Cidade: {student['city']}")

            return

    print(f"O estudante {name} não foi encontrado.")



def edit_student():

    name = input("Digite o nome do estudante que deseja editar: ")

    for student in students:

        if student['name'] == name:

            new_name = input("Digite o novo nome (ou pressione Enter para manter o atual): ")

            new_age = input("Digite a nova idade (ou pressione Enter para manter a atual): ")

            new_city = input("Digite a nova cidade (ou pressione Enter para manter a atual): ")

            

            if new_name:

                student['name'] = new_name

            if new_age:

                student['age'] = new_age

            if new_city:

                student['city'] = new_city



            print(f"Estudante {name} atualizado com sucesso.")

            return

    print(f"O estudante {name} não foi encontrado.")



def remove_student():

    name = input("Digite o nome do estudante que deseja remover: ")

    for student in students:

        if student['name'] == name:

            students.remove(student)

            print(f"Estudante {name} removido com sucesso.")

            return

    print(f"O estudante {name} não foi encontrado.")



# Início do programa

while True:

    menu()

    option = input("Escolha uma opção: ")



    if option == '1':

        add_student()

    elif option == '2':

        list_students()

    elif option == '3':

        search_student()

    elif option == '4':

        edit_student()

    elif option == '5':

        remove_student()

    elif option == '6':

        print("Saindo do sistema...")

        break

    else:

        print("Opção inválida. Tente novamente.")
