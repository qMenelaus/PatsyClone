import json
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Configurações das contas do Telegram
api_id1 = 'YOUR_API_ID_1'
api_hash1 = 'YOUR_API_HASH_1'
phone1 = 'YOUR_PHONE_NUMBER_1'

api_id2 = 'YOUR_API_ID_2'
api_hash2 = 'YOUR_API_HASH_2'
phone2 = 'YOUR_PHONE_NUMBER_2'

api_id3 = 'YOUR_API_ID_3'
api_hash3 = 'YOUR_API_HASH_3'
phone3 = 'YOUR_PHONE_NUMBER_3'

api_id4 = 'YOUR_API_ID_4'
api_hash4 = 'YOUR_API_HASH_4'
phone4 = 'YOUR_PHONE_NUMBER_4'

source_chat = 'SOURCE_CHAT_ID'  # ID do chat de origem
destination_chat = 'DESTINATION_CHAT_ID'  # ID do chat de destino

# Renomear o arquivo JSON com base no chat de origem
json_file = f'sync({source_chat}).json'

# Função para carregar IDs de mensagens copiadas
def load_copied_message_ids():
    try:
        with open(json_file, 'r') as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

# Função para salvar IDs de mensagens copiadas
def save_copied_message_ids(message_ids):
    with open(json_file, 'w') as f:
        json.dump(list(message_ids), f)

# Função para limpar o arquivo JSON
def clear_copied_message_ids():
    with open(json_file, 'w') as f:
        json.dump([], f)

# Função para perguntar ao usuário sobre a clonagem
def ask_user_choice():
    while True:
        choice = input("Você deseja continuar uma clonagem existente(y) ou iniciar uma nova(n)? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Escolha inválida. Por favor, digite 'y' para continuar ou 'n' para uma nova.")

# Inicialização dos clientes do Telegram
client1 = TelegramClient('session1', api_id1, api_hash1)
client2 = TelegramClient('session2', api_id2, api_hash2)
client3 = TelegramClient('session3', api_id3, api_hash3)
client4 = TelegramClient('session4', api_id4, api_hash4)

async def forward_media_message(client, message, destination):
    if message.photo:
        await client.send_file(destination, message.photo, caption=message.text if message.text else '')
    elif message.video:
        await client.send_file(destination, message.video, caption=message.text if message.text else '')

async def main():
    await client1.start(phone1)
    await client2.start(phone2)
    await client3.start(phone3)
    await client4.start(phone4)
    
    try:
        if not await client1.is_user_authorized():
            await client1.send_code_request(phone1)
            await client1.sign_in(phone1, input('Enter the code for account 1: '))
            if not await client1.is_user_authorized():
                await client1.sign_in(password=input('Enter 2FA password for account 1: '))
        
        if not await client2.is_user_authorized():
            await client2.send_code_request(phone2)
            await client2.sign_in(phone2, input('Enter the code for account 2: '))
            if not await client2.is_user_authorized():
                await client2.sign_in(password=input('Enter 2FA password for account 2: '))

        if not await client3.is_user_authorized():
            await client3.send_code_request(phone3)
            await client3.sign_in(phone3, input('Enter the code for account 3: '))
            if not await client3.is_user_authorized():
                await client3.sign_in(password=input('Enter 2FA password for account 3: '))

        if not await client4.is_user_authorized():
            await client4.send_code_request(phone4)
            await client4.sign_in(phone4, input('Enter the code for account 4: '))
            if not await client4.is_user_authorized():
                await client4.sign_in(password=input('Enter 2FA password for account 4: '))
    except SessionPasswordNeededError:
        print("2FA required. Please set up your accounts with proper 2FA settings.")
        return
    
    user_choice = ask_user_choice()
    
    if user_choice == 'n':
        clear_copied_message_ids()
    
    copied_message_ids = load_copied_message_ids()
    total_messages_forwarded = 0

    # Se houver mensagens já copiadas, obter o ID da mensagem mais recente copiada
    if copied_message_ids:
        last_copied_message_id = max(copied_message_ids)
    else:
        last_copied_message_id = 0
    
    async for message in client1.iter_messages(source_chat, offset_id=last_copied_message_id, reverse=True):
        if message.id not in copied_message_ids and (message.photo or message.video):
            await forward_media_message(client1, message, destination_chat)
            copied_message_ids.add(message.id)
            total_messages_forwarded += 1
            print(f"Profile 1 enviou ID {message.id}. Total já enviado: {total_messages_forwarded}")
            await asyncio.sleep(3.5)
            
            async for message in client2.iter_messages(source_chat, offset_id=message.id-1, reverse=True):
                if message.id not in copied_message_ids and (message.photo or message.video):
                    await forward_media_message(client2, message, destination_chat)
                    copied_message_ids.add(message.id)
                    total_messages_forwarded += 1
                    print(f"Profile 2 enviou ID {message.id}. Total já enviado: {total_messages_forwarded}")
                    await asyncio.sleep(3.5)
                    break

            async for message in client3.iter_messages(source_chat, offset_id=message.id-2, reverse=True):
                if message.id not in copied_message_ids and (message.photo or message.video):
                    await forward_media_message(client3, message, destination_chat)
                    copied_message_ids.add(message.id)
                    total_messages_forwarded += 1
                    print(f"Profile 3 enviou ID {message.id}. Total já enviado: {total_messages_forwarded}")
                    await asyncio.sleep(3.5)
                    break

            async for message in client4.iter_messages(source_chat, offset_id=message.id-3, reverse=True):
                if message.id not in copied_message_ids and (message.photo or message.video):
                    await forward_media_message(client4, message, destination_chat)
                    copied_message_ids.add(message.id)
                    total_messages_forwarded += 1
                    print(f"Profile 4 enviou ID {message.id}. Total já enviado: {total_messages_forwarded}")
                    await asyncio.sleep(3.5)
                    break

    save_copied_message_ids(copied_message_ids)

    await client1.disconnect()
    await client2.disconnect()
    await client3.disconnect()
    await client4.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
