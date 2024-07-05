# 📬 Telegram Message Forwarding Script
> [!NOTE]
> Status: Developing

 Este script usa a biblioteca `Telethon` para clonar e encaminhar mensagens de mídia de um chat do Telegram para outro. 

## 📋 Funcionalidades
+ Possibilidade de 4 contas
+ Maior rapidez
+ Ponto de restauração
+ Quatro contas = 16msg/min

### 📃 Dependências:

Certifique-se de ter o `Telethon` instalado. Você pode instalá-lo via pip:
```
pip install telethon
```

## ⚙️ Configurações do Telegram:
Substitua `API_ID`,`HASH_ID` e `PHONE` no script main.py pelas suas credenciais e números de telefone do Telegram.

> [!IMPORTANT]
> Substitua os IDs dos chats de origem e destino pelos IDs apropriados.

Você pode usar o [64Gram](https://github.com/TDesktop-x64) para conseguir o `chat_id`.

+ source_chat = ` SOURCE_CHAT_ID`  # ID do chat de origem
+ destination_chat = ` DESTINATION_CHAT_ID`   # ID do chat de destino

### 🚀 Uso:
Execute o script no seu ambiente de desenvolvimento:
``` python main.py```

### 🔐 Processo de Autenticação:

O script irá pedir para você entrar com os códigos de verificação enviados para os números de telefone configurados.
Se necessário, você também será solicitado a inserir as senhas de 2FA.

Escolher Opção de Clonagem:
> [!NOTE]
> Status: Developing

Quando solicitado, escolha se deseja continuar uma clonagem existente (y) ou iniciar uma nova (n).


### 🔒 Segurança:

Sleep: O script tem um tempo de espera de 3,5 segundos entre cada mensagem serve para evitar problemas de rate limiting. Ajuste conforme necessário.
O tempo de 3,5 segundos é baseado na utilização de quatro contas.
Para fins de cálculo:
`sleep = 15segundos/n`
n = número de contas

### 🤝 Contribuição:
Se você quiser contribuir para este projeto, sinta-se à vontade para abrir issues ou enviar pull requests.

### 📜 Licença:
Este projeto está licenciado sob os termos da licença MIT.
