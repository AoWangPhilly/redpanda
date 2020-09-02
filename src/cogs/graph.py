import discord
from discord.ext import commands
from matplotlib import animation
from sympy.plotting import *
from utility.math_parser import parse_eq


class Graph(commands.Cog):
    """
    Contains various algebra tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.graph_location = 'temp/graph.png'
        self.parametric_graph_location = 'temp/parametric_graph.png'

    @commands.command()
    async def graph(self, ctx, *, eq: parse_eq):
        """Graphs simple equations"""
        p1 = plot(eq, show=False)
        p1.save(self.graph_location)
        await ctx.send(file=discord.File(self.graph_location))

    @commands.command()
    async def graph3d(self, ctx, *, eq: parse_eq):
        """Graphs equations in 3d"""
        p1 = plot3d(eq, show=False)
        p1.save(self.graph_location)
        await ctx.send(file=discord.File(self.graph_location))

    @commands.command(name='pgraph')
    async def p_graph(self, ctx, x: parse_eq, y: parse_eq):
        """
        Graph parametric equations
        Uses a single parameter
        """
        p1 = plot_parametric(x, y)
        p1.save(self.parametric_graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))

    @commands.command(name='pgraph3dline')
    async def p_graph_line(self, ctx, x: parse_eq, y: parse_eq, z: parse_eq):
        """
        Graph 3d parametric equations in line form
        Uses a single parameter
        """
        p1 = plot3d_parametric_line(x, y, z)
        p1.save(self.parametric_graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))

    @commands.command(name='pgraph3dsurface')
    async def p_graph_surface(self, ctx, x: parse_eq, y: parse_eq, z: parse_eq):
        """
        Graph 3d parametric equations in surface form
        Uses two parameters
        """
        p1 = plot3d_parametric_surface(x, y, z)
        p1.save(self.parametric_graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))

    @commands.command(name='pgraphgif')
    async def p_graph_gif(self, ctx):
        """
        Graph 3d parametric equations in surface form
        Uses two parameters
        """
        import numpy as np
        import matplotlib.pyplot as plt

        plt.rcParams['legend.fontsize'] = 10

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        def rotate(angle):
            ax.view_init(azim=angle)

        # Prepare arrays x, y, z
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
        z = np.linspace(-2, 2, 100)
        r = z ** 2 + 1
        x = r * np.sin(theta)
        y = r * np.cos(theta)

        ax.plot(x, y, z, label='parametric curve')
        ax.legend()
        rotation = animation.FuncAnimation(
            fig, rotate, frames=np.arange(0, 362, 2), interval=100)
        rotation.save('temp/rotation.gif', dpi=80, writer='imagemagick')

        await ctx.send(file=discord.File('temp/rotation.gif'))
