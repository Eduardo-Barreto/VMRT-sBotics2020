import os
import datetime


file_name = input('Digite o nome do arquivo final (sem a extensão): ')


while True:

    directory = os.listdir('./src')

    if 'output' not in os.listdir('./'):
        os.mkdir('./output')

    out = open('./output/'+file_name+'.sBoticsR', 'w')

    data = datetime.datetime.now()

    out.write('#Ofere.ci.mentos\n#SESI VMRT - SP\n#Last change: ' + str(data.strftime("%d")) + '/' + str(data.strftime("%m")) + '/' + str(data.strftime("%Y")) + ' | ' + str(data.strftime("%X")) + '\n\n')
    out.write('#Disponivel em: https://github.com/Eduardo-Barreto/VMRT-sBotics\n')
    out.write('#'+'-'*100+'\n')

    os.system('cls')

    for source_file in directory:
        if 'sBoticsR' in source_file:
            current_file = open('./src/' + source_file, 'r')
            for line in current_file:
                if '#' not in line:
                    if 'escrever' not in line:
                        if 'limparconsole' not in line:
                            if line != '':
                                out.write(line)
            current_file.close()

        else:
            print('-'*20, 'Arquivo inválido:', source_file, '-'*20, end='')
        print('\n', '-'*20, 'Arquivo',
              source_file[:source_file.find('.sBoticsR')],
              'compilado com sucesso', '-'*20)

    out.write('fim\n')
    out.write('#'+'-'*100)
    out.write('\n#Ofere.ci.mentos\n#SESI VMRT - SP\n#Last change: ' + str(data.strftime("%d")) + '/' + str(data.strftime("%m")) + '/' + str(data.strftime("%Y")) + ' | ' + str(data.strftime("%X")) + '\n\n')
    out.write('#Disponivel em: https://github.com/Eduardo-Barreto/VMRT-sBotics')
    out.close()
    print('\nDigite compilar para compilar novamente\n')
    while input() != 'compilar':
        pass
