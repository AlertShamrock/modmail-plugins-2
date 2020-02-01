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
            description="__Say ***THESE*** commands in ***THIS*** channel **ONLY!**__",
        )
        embed.add_field(name="__Update your Discord rank__",value="Say this command `!getroles`")
        embed.add_field(name="__Report__",value="Reporting a Discord User! **Command** `?report <Discord User> <Reason>`")
        ##embed.add_field(name="__Inactivity notice__",value="Going on vacation, or not going be on base? \n **Say these commands** \n
##`!apply`\n **NOTE:** Can be demoted until HQ (Head Quarters) approves of your inactivity request.")
      ##  embed.add_field(name="__Suggestions__",value="Want to suggest something to Army discord or on to a base? \n **Say these commands** \n **Add these before you MESSAGE** \n ***Message Prefix*** \n `[BASE]` \n `[DISCORD]` \n `[GROUP]` \n **Command:** \n`!suggest (PREFIX) (message)`")
        embed.add_field(name="__Quote__",value="Add a quote onto quotes channel! **Command** `!quote <Quote here>`")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
