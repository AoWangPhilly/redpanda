import discord
from discord.ext import commands
import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector

def convert(vec):
    vec = vec.replace('<', '').replace('>', '').split(',')
    return Matrix(list(map(int, vec)))

class Vector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dot(self, ctx, v1 : convert, v2 : convert):
        '''Computes dot product'''
        await ctx.send(v1.dot(v2))

    @commands.command()
    async def cross(self, ctx, v1 : convert, v2 : convert):
        '''Computes cross product'''
        C = CoordSys3D('')
        cp = matrix_to_vector(v1.cross(v2), C)
        sympy.preview(cp, viewer='file', filename='vector.png')
        await ctx.send(file=discord.File('vector.png'))

