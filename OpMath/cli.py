from OpMath import *

import click

@click.command()
@click.option("-n",'--num', type= int, help='specificy a number', required=True)

def main():
    result1 = square(num)
    result2 = double(num)
    print(f"The square of {num} is {result1}")
    print(f"The double of {num} is {result2}")

if __name__ == '__main__':
    main()