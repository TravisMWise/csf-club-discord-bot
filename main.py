# CSF Discord Bot
# Travis M Wise
# 8-11-2021

# Imports
import discord
import os

# !inspire imports
import requests
import json

# keep alive import
from keep_alive import keep_alive

client = discord.Client()
# On ready event
@client.event
async def on_ready():
  print("Bot is online. Username: {0.user}".format(client))


# Get a quote from https://zenquotes.io/api/random and return it
def get_quote():
  response  = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

# Events for when a user sends a message
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content # Store the message sent in msg
  UserID = message.author.id # Store the ID of the user in UserID
  #UserName = message.author.name # Store the name of the user in UserName
  msgID = '<@' + str(UserID) + '>' # Format the UserID to @ them in discord

  if msg.startswith("!inspire"):
    quote = get_quote()
    await message.channel.send("Hello " + msgID + "! Here is your inspirational quote:\n" + quote)
    return

  if msg.startswith("!help"):
    intro = "Hello " + msgID + "! Here is a list of all the commands you can use to find out more about the CSF Club!\n"
    with open('help.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!registration"):
    intro = "Hello " + msgID + "! The following are the registration steps for the club:\n"
    with open('registration.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!forms"):
    intro = ("Hello " + msgID + "! Here is a list of all the forms and links useful for registering:\n")
    with open('forms.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!about"):
    intro = ("Hello " + msgID + "!\n")
    with open('about.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!dues"):
    intro = ("Hello " + msgID + "! Here is the breakdown for the dues for the club:\n")
    with open('dues.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!faq"):
    intro = ("Hello " + msgID + "! This is the list of frequently asked questions we have to help make the registration process smother!\n")
    with open('faq.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!current_projects"):
    intro = ("Hello " + msgID + "!\n")
    with open('current_projects.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  if msg.startswith("!website"):
    intro = ("Hello " + msgID + "!\n")
    with open('website.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'
    await message.channel.send(intro + output)
    return

  '''if msg.startswith("!socials"):
    intro = ("Hello " + msgID + "!\n")
    with open('socials.txt', 'r') as fp:
      lines = fp.readlines()
    output = '```'
    for line in lines:
      output += line
    output += '```'

    await message.channel.send(intro + output)
    return'''''

# keep keep_alive
keep_alive()
# Turn on the bot
client.run(os.environ["TOKEN"])
