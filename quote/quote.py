import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class Quote(commands.Cog):
    """
    Let's you send a quote to a designated channel.
    """
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.command(aliases = ['qu'])
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def setquotechannel(self, ctx, channel: discord.TextChannel):
        """
        Set the channel where quotes go.
        """
        await self.coll.find_one_and_update(
            {"_id": "config"},
            {"$set": {"quote-channel": {"channel": str(channel.id)}}},
            upsert=True,
        )
        embed=discord.Embed(title=f'Set quote channel to {channel}.', color=0x4dff73)
        embed.set_author(name="Success!")
        embed.set_footer(text="Task succeeded successfully.")
        await ctx.send(embed=embed)

    @commands.command()
    async def quote(self, ctx, *, quote):
        """
        Quote something!
        """
        async with ctx.channel.typing():
            config = await self.coll.find_one({"_id": "config"})
            if config is None:
                embed=discord.Embed(title="quote channel not set.", color=self.bot.error_colour)
                embed.set_author(name="Error.")
                embed.set_footer("Task failed successfully.")
                await ctx.send(embed=embed)
            else:
                quote_channel = self.bot.get_channel(int(config["quote-channel"]["channel"]))
                
                embed=discord.Embed(title=quote, color=self.bot.main_color)
                embed.set_author(name=f"Quote sent by {ctx.author}:", icon_url=ctx.author.avatar_url)
                embed.set_footer(text="Say ?quote <Message here> to send a quote!")
                await quote_channel.send(embed=embed)
                
                await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

def setup(bot):
    bot.add_cog(Quote(bot))
