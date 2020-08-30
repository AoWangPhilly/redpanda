import discord
from discord.ext import commands
import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector


class Vector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dot(self, ctx, v1, v2):
        '''Computes dot product, i.e. !dot <1,2,3> <4,5,6>'''
        v1, v2 = self.convert(v1), self.convert(v2)
        await ctx.send(v1.dot(v2))

    @commands.command()
    async def cross(self, ctx, v1, v2):
        '''Computes cross product, i.e. !cross <1,2,3> <4,5,6>'''
        C = CoordSys3D('')
        v1, v2 = self.convert(v1), self.convert(v2)
        cp = matrix_to_vector(v1.cross(v2), C)
        sympy.preview(cp, viewer='file', filename='vector.png')
        await ctx.send(file=discord.File('vector.png'))

    def convert(self, vec):
        vec = vec.replace('<', '').replace('>', '').split(',')
        return Matrix(list(map(int, vec)))
