# 📜 Histórico de Pedidos - Consulta e Busca
# Sistema para visualizar e filtrar pedidos salvos em arquivos TXT

import os

# --- Banco de Dados Local ---
ARQUIVO_USUARIOS = 'usuarios.txt'

# Garante que o arquivo de usuários exista
if os.path.exists(ARQUIVO_USUARIOS) == False:
    open(ARQUIVO_USUARIOS, 'w', encoding='utf-8').close()

# --- Cores ANSI ---
RESET = '\033[0m'
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
ROXO = '\033[95m'
CIANO = '\033[96m'
BRANCO = '\033[97m'

# --- Cabeçalho ---
print(f'{AZUL}╔════════════════════════════════════╗{RESET}')
print(f'{AZUL}║{BRANCO}         HISTÓRICO DE PEDIDOS       {AZUL}║{RESET}')
print(f'{AZUL}╚════════════════════════════════════╝{RESET}')
print(f'{CIANO}Você precisa fazer login para ver seu histórico.{RESET}\n')

acesso_liberado = False
usuario_logado = ''

# --- Login para Acesso ao Histórico ---
for tentativa in range(1, 4):
    print(f'{AMARELO}Tentativa {tentativa} de 3{RESET}')
    usuario = input(f'{BRANCO}Usuário: {RESET}').strip().lower()
    senha = input(f'{BRANCO}Senha: {RESET}').strip()

    with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if ';' in linha:
                usuario_salvo, senha_salva = linha.split(';', 1)
                if usuario == usuario_salvo and senha == senha_salva:
                    acesso_liberado = True
                    usuario_logado = usuario
                    break

    if acesso_liberado == True:
        break
    else:
        print(f'\n{VERMELHO}Usuário ou senha incorretos.{RESET}')
        if tentativa < 3:
            print(f'{AMARELO}Tente novamente.\n{RESET}')
        else:
            print(f'{VERMELHO}Fim das tentativas.\n{RESET}')

# --- Visualização do Histórico ---
if acesso_liberado == False:
    print(f'{VERMELHO}Sem acesso ao histórico.{RESET}')
else:
    arquivo_pedidos = 'pedidos_{}.txt'.format(usuario_logado)
    if os.path.exists(arquivo_pedidos) == False:
        open(arquivo_pedidos, 'w', encoding='utf-8').close()

    print(f'{ROXO}╔════════════════════════════════════╗{RESET}')
    print(f'{ROXO}║{BRANCO}        HISTÓRICO DO USUÁRIO        {ROXO}║{RESET}')
    print(f'{ROXO}╚════════════════════════════════════╝{RESET}\n')

    with open(arquivo_pedidos, 'r', encoding='utf-8') as arquivo:
        pedidos = arquivo.readlines()

    if len(pedidos) == 0:
        print(f'{AMARELO}Nenhum pedido encontrado para {usuario_logado}.{RESET}')
    else:
        print(f'{CIANO}Usuário: {usuario_logado}{RESET}\n')
        
        contador = 0
        for linha in pedidos:
            contador = contador + 1
            print(f'{AZUL}{contador} - {linha.strip()}{RESET}')

        # --- Opções de Busca/Filtro ---
        print(f'\n{AMARELO}Formas de busca:{RESET}')
        print(f'{CIANO}1 - Buscar por item | 2 - Buscar por pagamento | 3 - Sair{RESET}\n')

        escolha = input(f'{BRANCO}Escolha: {RESET}').strip()

        if escolha in ['1', '2']:
            termo = 'item' if escolha == '1' else 'forma de pagamento'
            busca = input(f'{BRANCO}Digite o que deseja buscar ({termo}): {RESET}').strip().lower()
            encontrados = 0

            print(f'\n{ROXO}╔════════════════════════════════════╗{RESET}')
            print(f'{ROXO}║{BRANCO}         RESULTADO DA BUSCA         {ROXO}║{RESET}')
            print(f'{ROXO}╚════════════════════════════════════╝{RESET}\n')

            contador = 0
            for linha in pedidos:
                contador = contador + 1
                if busca in linha.lower():
                    encontrados = encontrados + 1
                    print(f'{CIANO}{contador} - {linha.strip()}{RESET}')

            if encontrados == 0:
                print(f'{VERMELHO}Nada encontrado para "{busca}".{RESET}')
        else:
            print(f'\n{VERDE}Consulta finalizada.{RESET}')

print(f'\n{AZUL}Fim do histórico.{RESET}')
