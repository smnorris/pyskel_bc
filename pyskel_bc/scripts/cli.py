# Skeleton of a CLI

import click

import pyskel_bc


@click.command('pyskel_bc')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(pyskel_bc.has_legs)
