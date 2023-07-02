from discord import Intents
from discord.ext import commands
from flask import Flask, render_template
from replit import db
from typing import Optional
from os import environ

intents = Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

app = Flask(__name__)
bot = commands.Bot(command_prefix="$", intents=intents)

@app.route('/')
def index():
  return render_template("index.html"))

app.run('0.0.0.0', port=81)
