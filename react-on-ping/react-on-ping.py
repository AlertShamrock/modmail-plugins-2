import discord
from discord.ext import commands

class ReactOnPing(commands.Cog):
    """Reacts with a ping emoji when someone gets pinged."""
    emojis = [
    "shamrock:
    ]

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if '<@412762426132398102>' in message.content.upper():
            ctrx.channel.send("If you need help please DM me! Please do not PING/MENTION staff")
            for emoji in self.emojis:
                await message.add_reaction(emoji)

def setup(bot):
    bot.add_cog(ReactOnPing(bot))
