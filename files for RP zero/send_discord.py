

ENABLE_DISCORD_LOGGING = False
YOUR_TOKEN = "Your Token" #Write Your discord bot token here:
YOUR_CHANNEL_ID = 1235969503771361332 #Write the channel in which you want the bot to write here (takes an integer):

if ENABLE_DISCORD_LOGGING:
    import discord
    import time
    import aiohttp
    import asyncio
    import datetime
    import os
    from aiohttp import connector

    check_delay_seconds = 10
    buffer = ""
    first_message_id = None
    current_directory = os.path.dirname(os.path.realpath(__file__))
    buffer_path = current_directory+"/discord_buffer.txt"



    intents = discord.Intents.default()
    intents.messages = True
    client = discord.Client(intents=intents)

    #user = client.get_user(YOUR_USER_ID)
    def chunk_string(string, chunk_size):
        return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

    async def send_message_to_channel(channel_id:int,message:str):
        
        await client.wait_until_ready() 
        
        channel = client.get_channel(channel_id)
        
        if channel:
            message = await channel.send(message)
            print("message_sent")
            return message.id
    async def add_to_message(string_to_add, message_id, channel_id):
        global first_message_id
        
            
        message = await client.get_channel(channel_id).fetch_message(message_id)
        message_contents = message.content
            
        new_message_contents = message_contents + string_to_add
            
        new_message_chunks = chunk_string(new_message_contents, 1990)
            
        await message.edit(content=new_message_chunks[0])
        new_message_chunks = new_message_chunks[1:]
            
        while new_message_chunks:
            message_id = await send_message_to_channel(YOUR_CHANNEL_ID,"[next]")
            message = await client.get_channel(channel_id).fetch_message(message_id)
            await message.edit(content=new_message_chunks[0])
            new_message_chunks = new_message_chunks[1:]
        first_message_id = message_id
            
        

    def clear_txt_buffer(length:int):

        if os.path.exists(buffer_path):
            with open(buffer_path,"r+") as file:
                content = file.read()
                file.seek(0)
                file.write(content[length:])
                file.truncate()
                print(file.read())

                


    def read_txt_buffer_contents():
        if os.path.exists(buffer_path):
            with open(buffer_path,"r") as file:
                return file.read()
        return ""



    @client.event
    async def on_ready():
        global buffer
        global first_message_id
        global YOUR_CHANNEL_ID
        
        first_message_id = await send_message_to_channel(channel_id=YOUR_CHANNEL_ID,message="[start]")
        
        #send the first message that will be edited
        

        
        while True:
            
            try:
                await asyncio.sleep(check_delay_seconds)
                
                #print(f'We have logged in as {client.user}')
                if buffer:

                    await add_to_message(buffer,first_message_id, YOUR_CHANNEL_ID)
                    clear_txt_buffer(len(buffer))
                    buffer = ""
                    
                buffer += read_txt_buffer_contents()

                
            except discord.errors.HTTPException:
                await asyncio.sleep(check_delay_seconds)
            except KeyboardInterrupt as e:
                quit()
            except aiohttp.client_exceptions.ClientConnectorError:
                await asyncio.sleep(check_delay_seconds)
            except Exception as e:
                await asyncio.sleep(check_delay_seconds)


    def run_bot():
        try:
            client.run(YOUR_TOKEN, reconnect=True, log_handler=None)
        except Exception as e:
            return