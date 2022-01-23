import discord
from discord.utils import get
import os
import schedule
import time
import random
from dotenv import load_dotenv
load_dotenv()


client = discord.Client()
count = client.guilds
roles = ["Verdant Being","Sanguine Being","Azure Being"]
numroles = 3

def job():
    print("DOING")
    for guild in client.guilds:
            for count in client.guilds[guild].member_count:
                role = get(name=roles[random.randint(1,numroles)])
                client.add_roles(client.guilds.members[count], role)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
print("DO")
schedule.every(1).minutes.do(job)
print("ING")

client.run(os.getenv('Token'))