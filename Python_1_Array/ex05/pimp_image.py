import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_display_image(image: np.array, title: str, cmap: str = None):
    """
    Displays the image with the given title.
    """
    try:
        plt.imshow(image, cmap=cmap)
        plt.title(title)
        plt.axis('on')
        plt.show()
    except Exception as e:
        raise ValueError(f"Error occurred during displaying the image: {e}")


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the colors of the image.
    Args:
    array (np.array): The input image array.
    Returns:
    np.array: The color-inverted image array.
    """
    try:
        inverted_array = 255 - array
        ft_display_image(inverted_array, "Invert")
        return inverted_array
    except Exception as e:
        raise ValueError(f"Error during inverting the image: {e}")


def ft_red(array: np.array) -> np.array:
    """
    Applies a red color filter to the image.
    Args:
    array (np.array): The input image array.
    Returns:
    np.array: The color-filtered image array.
    """
    try:
        # init a array with the same shape as the input array,
        # but with all elements initialized to zero
        red_array = np.zeros_like(array)
        # indicates selection/copy of all rows and columns, but only the
        # first channel (index 0) corresponding the red channel in RGB format.
        red_array[:, :, 0] = array[:, :, 0]  # Red channel
        ft_display_image(red_array, "Red")
        return red_array
    except Exception as e:
        raise ValueError(f"Error during red filtering the image: {e}")


def ft_green(array: np.array) -> np.array:
    """
    Applies a green color filter to the image.
    Args:
    array (np.array): The input image array.
    Returns:
    np.array: The color-filtered image array.
    """
    try:
        green_array = np.zeros_like(array)
        # to modify the green channel, access index 1 in the last dimension
        # of the array RGB.
        green_array[:, :, 1] = array[:, :, 1]  # Green channel
        ft_display_image(green_array, "Green")
        return green_array
    except Exception as e:
        raise ValueError(f"Error during green filtering the image: {e}")


def ft_blue(array: np.array) -> np.array:
    """
    Applies a blue color filter to the image.
    Args:
    array (np.array): The input image array.
    Returns:
    np.array: The color-filtered image array.
    """
    try:
        blue_array = np.zeros_like(array)
        # this line copies the blue channel values from the original image
        # array to the blue channel of the new array, effectively applying
        # a blue color filter to the image.
        blue_array[:, :, 2] = array[:, :, 2]  # Blue channel
        ft_display_image(blue_array, "Blue")
        return blue_array
    except Exception as e:
        raise ValueError(f"Error during blue filtering the image: {e}")


def ft_grey(array: np.array) -> np.array:
    """
    Applies a grey color filter to the image.
    Args:
    array (np.array): The input image array.
    Returns:
    np.array: The color-filtered image array.
    """
    try:
        # sums the values of the third dimension (axis 2), which corresponds
        # to the color channels RGB, then we divided this sum by 3, and
        # now we have a value inside this only one channel that represents
        # the represents the intensity of light, with 0 being black, 255 being
        # white, and values in between representing various shades of grey.
        sum_array = array.sum(axis=2)
        grey_array = sum_array / 3
        ft_display_image(grey_array, "Grey", "gray")
        return grey_array
        """ Easier way, but using +
        red = array[:,:,0] / 3
        green = array[:,:,1] / 3
        blue = array[:,:,2] / 3
        grey_array = red + green + blue
        """
    except Exception as e:
        raise ValueError(f"Error during grey filtering the image: {e}")


"""
** In typical RGB (Red, Green, Blue) image arrays [height, width, rgb],
the last dimension represents the color channels, and their indexes are:
Index 0: Red channel
Index 1: Green channel
Index 2: Blue channel

** So, in ft_red, ft_green and ft_blue we are preserving only 1 channel
intensity values while discarding the intensity values (zero intensity)
of the other color channels.

** ft_invert: Uses = and -
by subtracting each value channel in array RGB from 255 (255 - array).

** ft_red: Uses =

** ft_green: Uses =

** ft_blue: Uses = by directly assigning the blue channel values.

ft_grey: Uses = and / by dividing the sum of RGB channels by 3 to
calculate the grayscale value for each pixel.

"""


def main():
    try:
        array = ft_load("../landscape.jpg")

        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

        print(ft_invert.__doc__)
        print(ft_red.__doc__)
        print(ft_green.__doc__)
        print(ft_blue.__doc__)
        print(ft_grey.__doc__)

    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
