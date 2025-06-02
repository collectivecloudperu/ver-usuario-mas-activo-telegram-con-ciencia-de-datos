from telethon.sync import TelegramClient
import pandas as pd, matplotlib.pyplot as plt

api_id = 00000000
api_hash = 'tu-hash'
client = TelegramClient('tu.usuario', api_id, api_hash)
grupo = 'tu-grupo-de-telegram'
limite = 1000

async def main():
    await client.start()
    entidad = await client.get_entity(grupo)
    msgs = [dict(user_id=m.sender_id, username=m.sender.username, date=m.date)
            async for m in client.iter_messages(entidad, limit=limite)
            if m.sender and m.sender.username]
    
    if not msgs:
        print("No se encontraron mensajes."); return
    
    df = pd.DataFrame(msgs)
    top = df['username'].value_counts().head(10)
    print("Usuarios más activos:\n", top)
    top.plot(kind='bar', title='Top 10 usuarios', color="skyblue")
    plt.xlabel('Usuario'); plt.ylabel('Mensajes')
    plt.tight_layout(); plt.savefig('top_usuarios.png'); plt.show()

with client: client.loop.run_until_complete(main())
