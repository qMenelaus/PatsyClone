# 📬 Telegram Message Forwarding Script

Este script usa a biblioteca `Telethon` para clonar e encaminhar mensagens de mídia de um chat do Telegram para outro. 

## ⚙️ Configuração:

### 📃 Dependências:

Certifique-se de ter o `Telethon` instalado. Você pode instalá-lo via pip:
```
pip install telethon
```

## ⚙️ Configurações do Telegram:
Substitua `API_ID`,`HASH_ID` e `PHONE` no script main.py pelas suas credenciais e números de telefone do Telegram.


Substitua os IDs dos chats de origem e destino pelos IDs apropriados:

source_chat = 'SOURCE_CHAT_ID'  # ID do chat de origem
destination_chat = 'DESTINATION_CHAT_ID'  # ID do chat de destino
## 🚀 Uso: 

Execute o script no seu ambiente de desenvolvimento:
``` python main.py```

## 🔐 Processo de Autenticação:

O script irá pedir para você entrar com os códigos de verificação enviados para os números de telefone configurados.
Se necessário, você também será solicitado a inserir as senhas de 2FA.

Escolher Opção de Clonagem
Quando solicitado, escolha se deseja continuar uma clonagem existente (y) ou iniciar uma nova (n).

## 📋 Funcionalidades
Carregar IDs de Mensagens Copiadas: Carrega os IDs das mensagens já copiadas a partir de um arquivo JSON.
Salvar IDs de Mensagens Copiadas: Salva os IDs das mensagens copiadas no arquivo JSON.
Limpar IDs de Mensagens Copiadas: Limpa o arquivo JSON para iniciar uma nova clonagem.
Encaminhar Mensagens de Mídia: Encaminha mensagens de mídia (fotos e vídeos) do chat de origem para o chat de destino, evitando duplicações.
## 🔒 Segurança:

Tempo de Espera: O script tem um tempo de espera de 3,5 segundos entre cada mensagem para evitar problemas de rate limiting. Ajuste conforme necessário.

## 🤝 Contribuição:
Se você quiser contribuir para este projeto, sinta-se à vontade para abrir issues ou enviar pull requests.

## 📜 Licença:
Este projeto está licenciado sob os termos da licença MIT.
