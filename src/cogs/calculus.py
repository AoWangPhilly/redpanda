import discord
from discord.ext import commands
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot

def parseEq(eq):
    eq = eq.replace('^', '**').replace('e', 'E')
    return parse_expr(eq)

class Calculus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def derive(self, ctx, *, eq: parseEq):
        '''Derives single variable equations'''
        sympy.preview(sympy.diff(eq), viewer='file',
                      filename='output.png', dvioptions=['-D', '200'])
        await ctx.send(file=discord.File('output.png'))

    @commands.command()
    async def integrate(self, ctx, *, eq: parseEq):
        '''Integrates single variable equations'''
        sympy.preview(sympy.integrate(eq), viewer='file',
                      filename='output.png', dvioptions=['-D', '200'])
        await ctx.send(file=discord.File('output.png'))

    @commands.command()
    async def graph(self, ctx, *, eq: parseEq):
        '''Graphs simple equations'''
        p1 = plot(eq, show=False)
        p1.save('graph.png')
        await ctx.send(file=discord.File('graph.png'))
