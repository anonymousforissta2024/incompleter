#Source: https://stackoverflow.com/questions/70234531/click-typeerror-init-missing-1-required-positional-argument-name
#!/usr/bin/python3
import click

@click.Command()
def main():
    print(f"hello world")
    
if __name__ == "__main__": 
    main()