import os
from PIL import Image
import typer


def resize_image():
    pass


def remove_bakground():
    pass


def save_jpg():
    pass


def save_png():
    pass


def main(
    path: str,
    resize: int = typer.Option(None, help="Width of the new image [in pixels]."),
    remove_bg: bool = typer.Option(False, help="Remove white background."),
):
    """Improve image efficency for web usage.
    """

    # Check path existance
    if not os.path.exists(path):
        typer.echo("ERROR: the provided path is not valid.")
        raise typer.Exit(1)

    img = Image.open(path)


if __name__ == "__main__":
    typer.run(main)
