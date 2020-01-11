import discord
from discord.ext import commands
from grammarbot import GrammarBotClient

class Grammar(commands.Cog):
    """Grammar checker."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Grammar(bot))