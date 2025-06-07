import discord
from discord.ext import commands
from discord import app_commands
from myserver import server_on  # ต้องมี myserver.py ด้วยนะ

import os

# เรียกใช้งาน Flask ให้ทำงานใน background
server_on()

# เปิดใช้งาน Intents
intents = discord.Intents.default()
intents.message_content = True  # จำเป็นหากจะอ่านข้อความ
intents.guilds = True
intents.members = True

# สร้าง Bot พร้อม Prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# สร้าง Slash Command Tree
tree = bot.tree

# อีเวนต์เมื่อบอทออนไลน์
@bot.event
async def on_ready():
    print(f"✅ บอทออนไลน์แล้วในชื่อ {bot.user} (ID: {bot.user.id})")
    print("------")
    try:
        synced = await tree.sync()
        print(f"🟢 ซิงค์ Slash Commands จำนวน {len(synced)} คำสั่งแล้ว")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการซิงค์คำสั่ง: {e}")

# Prefix Command ทดสอบ
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Slash Command ทดสอบ
@tree.command(name="hello", description="บอทจะทักทายคุณ")
async def hello_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"สวัสดีครับ {interaction.user.mention} 👋")

# ใส่ Token จริงของคุณตรงนี้
TOKEN = "YOUR_DISCORD_BOT_TOKEN"

# รันบอท
bot.run(TOKEN)