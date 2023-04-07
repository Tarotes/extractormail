import os
import re

emails = set()

# Itera sobre todos os arquivos na pasta atual
for file in os.listdir():
    # Verifica se o arquivo é .txt
    if file.endswith('.txt'):
        # Abre o arquivo
        with open(file, 'r') as f:
            # Lê todo o conteúdo do arquivo
            content = f.read()
            # Utiliza expressão regular para localizar os e-mails
            match = re.findall(r'[\w\.-]+@[\w\.-]+', content)
            # Adiciona os e-mails encontrados no set 'emails'
            emails.update(match)

# Cria um novo arquivo 'e-mails.txt' e escreve todos os e-mails encontrados
with open('e-mails.txt', 'w') as f:
    f.write('\n'.join(emails))
