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
            description="(__**Update your Discord rank**__
Say this command `!getroles`

__**Report**__
Reporting a Discord User!
**Command**
`?report <Discord User> <Reason>`

__**Inactivity notice**__
Going on vacation, or not going be on base?
**Say these commands**
`!apply`
`/apply`
**NOTE:** Can be demoted until HQ (Head Quarters) approves of your inactivity request.

__**Suggestions**__
Want to suggest something to Army discord or on to a base?
**Say these commands**
**Add these before you MESSAGE**
***Message Prefix***
`[BASE]`
`[DISCORD]`
`[GROUP]`

**Command:**
`!suggest (PREFIX) (message)`

__**Quote**__
Add a quote onto quotes channel!
**Command**
`!quote <Quote here>`

------------------------------------------------------------------------------------------
__Say ***THESE*** commands in ***THIS*** channel **ONLY!**__
------------------------------------------------------------------------------------------)",
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
