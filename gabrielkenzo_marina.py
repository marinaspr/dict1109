import os

os.system('cls')
#Gabriel Kenzo e Marina
tabela = []
registro = {
    'CPF' : 12312312312,
    'Nome' : "Jaimes",
    'Idade' :29
}

tabela.append(registro.copy())


def pedir():
     while True:
        try:
            cpf = int(input("Digite o CPF: "))
        except ValueError:
            break 
        for linha in tabela: 
            if linha['CPF'] == cpf:
                for k, v in registro.items():
                    print(f"{k}: {v}\n")
                try:
                    Nome = input("Nome: ")
                    registro['Nome'] = Nome
                except ValueError:
                    print("\n")
                try:
                    Idade = int(input("Idade: "))
                    print("Editado com Sucesso")
                except ValueError:
                    print("Editado com Sucesso")
                    
        else:
            Nome = input("Nome: ")
            registro['Nome'] = Nome
            Idade = int(input("Idade: "))
            registro['Idade'] = Idade
            print("Cadastrado com sucesso!")
            tabela.append(registro.copy())
                
           
          
                    


            

pedir()