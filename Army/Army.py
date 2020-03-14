import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class Army(commands.Cog):
    """
    Let's you send a announcements to a designated channel.
    """
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.command(aliases = ['ar'])
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def setarmychannel(self, ctx, channel: discord.TextChannel):
        """
        Set the channel where announcemnts go.
        """
        await self.coll.find_one_and_update(
            {"_id": "config"},
            {"$set": {"army-channel": {"channel": str(channel.id)}}},
            upsert=True,
        )
        embed=discord.Embed(title=f'Set announcement channel to {channel}.', color=0x4dff73)
        embed.set_author(name="Success!")
        embed.set_footer(text="Task succeeded successfully.")
        await ctx.send(embed=embed)

    @commands.command()
    async def ssu(self, ctx, *, message):
        """
        Start an Sever Start Up!
        """
        async with ctx.channel.typing():
            config = await self.coll.find_one({"_id": "config"})
            if config is None:
                embed=discord.Embed(title="SSU channel not set.", color=self.bot.error_colour)
                embed.set_author(name="Error.")
                embed.set_footer("Task failed successfully.")
                await ctx.send(embed=embed)
            else:
                army_channel = self.bot.get_channel(int(config["army-channel"]["channel"]))
                await army_channel.send("<@&673321318288195584>");
                embed=discord.Embed(title=SSU, color=self.bot.main_color)
                embed.set_author(name=f"By {ctx.author}:", icon_url=ctx.author.avatar_url)
                await army_channel.send(embed=embed)
                
                await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
                 @commands.command()
    async def training(self, ctx, *, message):
        """
       Training
        """
        async with ctx.channel.typing():
            config = await self.coll.find_one({"_id": "config"})
            if config is None:
                embed=discord.Embed(title="Training channel not set.", color=self.bot.error_colour)
                embed.set_author(name="Error.")
                embed.set_footer("Task failed successfully.")
                await ctx.send(embed=embed)
            else:
                army_channel = self.bot.get_channel(int(config["army-channel"]["channel"]))
                await army_channel.send("<@&659096050379915304>");
                embed=discord.Embed(title=Training, color=self.bot.main_color)
                embed.set_author(name=f"By {ctx.author}:", icon_url=ctx.author.avatar_url)
                await army_channel.send(embed=embed)
                
                await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')


def setup(bot):
    bot.add_cog(Army(bot))
