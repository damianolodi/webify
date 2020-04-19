import os
from PIL import Image
import numpy as np
import typer


def remove_background(img):
    """Remove the white background of the Image provided.

    The function remove the white background from the image. The algorithm is
    executed using the support of the numpy module to speed up computations.

    In the current version, only the pixel that are exactly pure white ([255, 255, 255]
    in the RGB space) are considered. Future versions will implement more sophisticated
    algorithms to deal also with nearly-white pixels.

    Parameters
    ----------
    img: Image object
        Image that should be modified.

    Returns
    -------
    img: Image object
        New image with the white background removed.
    """

    typer.echo("Remove white background from the image...")
    img = img.convert("RGBA")

    # Extract RGB data
    data = np.array(img)
    rgb = data[:, :, :3]

    # Prepare mask for white pixels
    white = [255, 255, 255]
    mask = np.all(rgb == white, axis=-1)

    # Make white pixels transparent
    transparent = [255, 255, 255, 0]
    data[mask] = transparent

    img = Image.fromarray(data)

    return img


def resize_image(img, resize):
    """Resize the image maintaining proportions
    
    When the resizing is applied, the Image.LANCZOS resample algotithm provided
    by the Pillow module is applied by deafult. This choiche is given by the
    fact that, even if it is the less perfomrmant, it produce the better results
    both in upscaling and downscaling.

    Parameters
    ----------
    img: Image object
        Image that should be modified.
    resize: int
        width of the new image. 

    Returns
    -------
    img: Image object
        New resized image.
    """

    # Calculate the new dimensions
    old_width, old_height = img.size
    new_width = resize
    new_height = round(new_width * old_height / old_width)
    new_size = (new_width, new_height)

    typer.echo("Resize the new image to {}x{}...".format(new_width, new_height))
    img = img.resize(new_size, resample=Image.LANCZOS)

    return img


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

    # Store variable for future reference
    allowed_formats = ["PNG", "JPEG"]
    format_ = img.format
    filename = img.filename

    if format_ not in allowed_formats:
        typer.echo("ERROR: image format not allowed. Use PNG or JPEG.")
        raise typer.Exit(2)

    # Remove the background of the image
    if remove_bg:
        img = remove_background(img)
        format_ = "PNG"

    if resize:
        img = resize_image(img, resize)


if __name__ == "__main__":
    typer.run(main)
