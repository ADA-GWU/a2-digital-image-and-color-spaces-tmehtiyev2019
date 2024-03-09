import cv2
import numpy as np
from skimage.color import deltaE_cie76
import argparse

# Define a function to handle mouse click events
def click_event(event, x, y, flags, params):
    # Check if left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        global picked_color
        # Retrieve the color of the clicked pixel and print it
        picked_color = image[y, x].tolist()
        print(f"Picked Color: {picked_color}")
        # Close the image window
        cv2.destroyAllWindows()

# Function to display the image and set up mouse callback for color picking
def pick_color_from_image(image_path):
    global image
    # Read the image from the given path
    image = cv2.imread(image_path)
    # Display the image in a window
    cv2.imshow("Image", image)
    # Assign the click event function to the image window
    cv2.setMouseCallback("Image", click_event)
    # Wait for a key press
    cv2.waitKey(0)

# Function to find and highlight similar colors in the image
def find_similar_colors_in_image(image, picked_color, threshold=50):
    # Convert the picked color to Lab color space for accurate color comparison
    picked_color_rgb = np.array([picked_color], dtype=np.uint8).reshape(1, 1, 3)
    picked_color_lab = cv2.cvtColor(picked_color_rgb, cv2.COLOR_RGB2Lab)[0][0]
    
    # Convert the entire image to Lab color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    
    # Calculate the difference in color (Delta E) for each pixel in the image
    delta_es = np.apply_along_axis(lambda lab_color: deltaE_cie76(picked_color_lab, lab_color), 2, lab_image)
    # Create a mask for pixels with similar color based on the threshold
    mask = delta_es < threshold
    
    # Copy the original image and apply the mask (highlight in green)
    result_image = image.copy()
    result_image[mask] = [0, 255, 0]
    
    return result_image

# Main function to run the color picker and highlighter
def main(image_path, threshold):
    global picked_color
    # Pick a color from the image
    pick_color_from_image(image_path)
    # Find and highlight similar colors in the image
    similar_colors_image = find_similar_colors_in_image(image, picked_color, threshold)
    # Display the result
    cv2.imshow("Similar Colors Highlighted", similar_colors_image)
    # Wait for a key press before closing
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Command-line interface setup
if __name__ == "__main__":
    # Create argument parser to parse command line arguments
    parser = argparse.ArgumentParser(description='Find and highlight similar colors in an image.')
    # Add argument for image path
    parser.add_argument('image_path', type=str, help='Path to the input image file')
    # Add argument for color similarity threshold (optional, with default value)
    parser.add_argument('--threshold', type=int, default=50, help='Threshold for color similarity. Default is 50.')
    # Parse arguments
    args = parser.parse_args()

    picked_color = []
    # Execute the main function with provided arguments
    main(args.image_path, args.threshold)
