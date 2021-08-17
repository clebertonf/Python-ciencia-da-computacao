
def filter_aprove():
    try:
        file = open("alunos.txt", mode='r')
        notas = []
        final_notas = []
        for line in file:
            notas.append(line.split())
        for nota in notas:
            if int(nota[1]) < 6:
                final_notas.extend(nota)
                
                file_list = open('alunos_reprovados.txt', mode='w')
                file_list.writelines(final_notas)
                file_list.close()
    except OSError:
        print("Erro, arquivo não existe")
    else:
        print("arquivo manipulado e fechado com sucesso")
        file.close()


filter_aprove()