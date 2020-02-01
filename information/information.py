import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Information(Cog):
    """Information plugin"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def information(self, ctx):
        """Information about this server."""

        embed = discord.Embed(
            title="__**Commands**__",
            color=self.bot.main_color,
            description="__**Update your Discord rank**__ /n Say this command `!getroles`",
        )
        embed.add_field(name="__Update your Discord rank__",value="**Command** \n `!getroles`", inline=false)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
