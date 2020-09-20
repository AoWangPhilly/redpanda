import discord
from discord.ext import commands
from matplotlib import animation
from sympy.plotting import *
from utility.math_parser import parse_eq

import numpy as np

class Graph(commands.Cog):
    """
    Contains various algebra tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.graph_location = 'temp/graph.png'
        self.gif_location = 'temp/rotation.gif'

    @commands.command()
    async def graph(self, ctx, eq: parse_eq):
        """Graphs simple equations"""
        p1 = plot(eq, show=False)

        await self.send_graph(ctx, p1, self.graph_location, False)

    @commands.command()
    async def graph3d(self, ctx, eq: parse_eq, show_gif=False):
        """Graphs equations in 3d"""
        p1 = plot3d(eq, show=False)

        await self.send_graph(ctx, p1, self.graph_location, show_gif)

    @commands.command(name='pgraph')
    async def p_graph(self, ctx, x: parse_eq, y: parse_eq):
        """
        Graph parametric equations
        Uses a single parameter
        """
        p1 = plot_parametric(x, y)

        await self.send_graph(ctx, p1, self.graph_location, False)

    @commands.command(name='pgraph3dline')
    async def p_graph_line(self, ctx, x: parse_eq, y: parse_eq, z: parse_eq, show_gif=False):
        """
        Graph 3d parametric equations in line form
        Uses a single parameter
        """
        p1 = plot3d_parametric_line(x, y, z)

        await self.send_graph(ctx, p1, self.graph_location, show_gif)

    @commands.command(name='pgraph3dsurface')
    async def p_graph_surface(self, ctx, x: parse_eq, y: parse_eq, z: parse_eq, show_gif=False):
        """
        Graph 3d parametric equations in surface form
        Uses two parameters
        """
        p1 = plot3d_parametric_surface(x, y, z)

        await self.send_graph(ctx, p1, self.graph_location, show_gif)

    async def send_graph(self, ctx, p1, file_location, show_gif):
        p1.save(file_location)

        if not show_gif:
            await ctx.send(file=discord.File(file_location))
        else:
            backend = p1._backend
            fig = backend.fig
            ax = fig.gca(projection='3d')

            rotation = animation.FuncAnimation(fig, lambda angle: ax.view_init(azim=angle), frames=np.arange(0, 360, 30), interval=500)
            rotation.save(self.gif_location, dpi=80, writer='imagemagick')

            await ctx.send(file=discord.File(self.gif_location))
