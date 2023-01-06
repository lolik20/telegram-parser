from telethon import TelegramClient, events, sync,errors
import time

async def send(accounts,sender,client):
    print('\033[92msend message\033[0m')
    writeStream = open("./accounts.txt","w")
    writeStream.write(f'{accounts}{sender.id};')
    writeStream.close()
    replyStream = open("./reply.txt",encoding="utf-8")
    replyMessages =replyStream.read().split(';')
    for reply in replyMessages:
        time.sleep(60)
        await client.send_message(sender.id,reply)



settingStream = open ("./settings.txt")
settings = settingStream.read().split(';')
api_id = int(settings[0])
api_hash = str(settings[1])
# host = "217.29.63.202" # a valid host
# port = 10745  # a valid port
# proxy = (socks.SOCKS5, host, port)
client = TelegramClient('session_name', api_id, api_hash)


wordsStream = open("./words.txt",encoding = 'utf-8')
words = wordsStream.read().split(';')
wordsStream.close()
client.start()
print('started!')

@client.on(events.NewMessage(client.get_dialogs()))
async def handler(event):
    print(event.raw_text)
    sender = await event.get_sender()
    readStream = open("./accounts.txt","r")
    accounts = readStream.read()
    readStream.close()
    if str(sender.id) not in accounts:
        for word in words:
            if word in event.raw_text.lower():
                try:
                    await send(accounts,sender,client) 
                except errors.PeerFloodError:
                    await send(accounts,sender,client)
client.run_until_disconnected()

