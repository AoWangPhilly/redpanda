import discord
from discord.ext import commands
import sympy
from sympy.parsing.sympy_parser import parse_expr
from cogs.math_parser import parse_eq, parse_var


class Calculus(commands.Cog):
    """
    Contains various calculus tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/output.png'

    @commands.command(pass_context=True, aliases=['D', 'd'])
    async def derive(self, ctx, *, eq: parse_eq, value=None):
        """Derives single variable equations"""
        sympy.preview(sympy.diff(eq), viewer='file',
                      filename=self.file_location, dvioptions=['-D', '200'])
        await ctx.send(file=discord.File(self.file_location))

    @commands.command(pass_context=True, aliases=['I', 'i'])
    async def integrate(self, ctx, *, eq: parse_eq, value=None):
        """Integrates single variable equations"""
        sympy.preview(sympy.integrate(eq), viewer='file',
                      filename=self.file_location, dvioptions=['-D', '200'])
        await ctx.send(file=discord.File(self.file_location))

    @commands.command(pass_context=True, aliases=['I2', 'i2'])
    async def double_integral(self, ctx, eq: parse_eq, order: parse_var):
        """Computes double integrals"""
        sympy.preview(sympy.integrate(eq, order[0], order[1]), viewer='file',
                      filename=self.file_location, dvioptions=['-D', '200'])
        await ctx.send(file=discord.File(self.file_location))

    @commands.command(pass_context=True, aliases=['I3', 'i3'])
    async def triple_integral(self, ctx, eq: parse_eq, order: parse_var):
        """Computes triple integrals"""
        sympy.preview(sympy.integrate(eq, order[0], order[1], order[2]), viewer='file',
                      filename=self.file_location, dvioptions=['-D', '200'])
        await ctx.send(file=discord.File(self.file_location))
