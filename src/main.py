from PIL import ImageGrab, Image, ImageFilter, ImageFile, ImageDraw
import sys
import pyperclip
from io import BytesIO

SIZES: tuple[int, int] = (1920, 1080)
SCREENSHOT_SIZE: tuple[int, int] = (1920//2, 1080//2)
BORDER_RADIUS: int = 12  # Define the border radius

def open_image(bgpath: str) -> ImageFile:
    with Image.open(bgpath) as im:
        return blur(im)

def make_screenshot(sizes: tuple[int, int]) -> Image:
    return ImageGrab.grab(bbox=(0, 0, sizes[0], sizes[1]))

def blur(image: ImageFile) -> Image:
    return image.filter(ImageFilter.BLUR)

def resize_image(image: Image, size: tuple[int, int]) -> Image:
    return image.resize(size, Image.LANCZOS)

def paste_image(background: Image, foreground: Image, position: tuple[int, int]) -> Image:
    background.paste(foreground, position, foreground)
    return background

def create_rounded_mask(size: tuple[int, int], radius: int) -> Image:
    width, height = size
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, width, height), radius, fill=255)
    return mask

def main(bg_path: str, copy_to_clipboard: bool, show_image: bool) -> None:
    background = open_image(bg_path)
    screenshot = make_screenshot(SIZES)
    resized_screenshot = resize_image(screenshot, SCREENSHOT_SIZE)

    # Create a mask with rounded corners
    mask = create_rounded_mask(SCREENSHOT_SIZE, BORDER_RADIUS)
    resized_screenshot.putalpha(mask)

    # Define the position where the screenshot will be placed on the background
    position = (166, 80)  # Example position (center of the background image)

    final_image = paste_image(background, resized_screenshot, position)

    if show_image:
        final_image.show()  # Display the final image

    if copy_to_clipboard:
        """
        # Copy the image to the clipboard
        output = BytesIO()
        final_image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        pyperclip.copy(data)
        """
        print("Copy to buffer doesn't support now")
    else:
        final_image.save("final_image.png")  # Save the final image

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <background_image_path> [-b] [-s]")
        sys.exit(1)

    bg_path = sys.argv[1]
    copy_to_clipboard = '-b' in sys.argv
    show_image = '-s' in sys.argv

    main(bg_path, copy_to_clipboard, show_image)
