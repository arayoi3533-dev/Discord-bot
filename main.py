import discord
from discord.ext import tasks
import datetime
import os

# Koyebの設定で入れるトークンを読み込む設定
TOKEN = os.getenv('0m23nprf0ukrn6pwpz13i74layw5i86yuhhm7bop76fazhj62b11wv5qv5e82zwf')
# 【重要】ここに自分のDiscordのチャンネルID（数字）を入れる
CHANNEL_ID = 1455035197962584215 

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

    async def setup_hook(self):
        self.daily_announcement.start()

    @tasks.loop(minutes=30)
    async def daily_announcement(self):
        # 日本時間を取得
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        # 毎朝 8:00〜8:30 の間に1回だけ発言
        if now.hour == 8 and now.minute < 30:
            channel = self.get_channel(CHANNEL_ID)
            if channel:
                today = now.strftime('%m月%d日')
                await channel.send(f"おはようございます！今日は {today} です。")

    @daily_announcement.before_loop
    async def before_announcement(self):
        await self.wait_until_ready()

bot = MyBot()
bot.run(TOKEN)
