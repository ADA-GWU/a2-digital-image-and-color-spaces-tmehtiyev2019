import cv2
import numpy as np
from skimage.color import deltaE_cie76
import argparse

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global picked_color
        picked_color = image[y, x].tolist()
        print(f"Picked Color: {picked_color}")
        cv2.destroyAllWindows()

def pick_color_from_image(image_path):
    global image
    image = cv2.imread(image_path)
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", click_event)
    cv2.waitKey(0)

def find_similar_colors_in_image(image, picked_color, threshold=50):
    picked_color_rgb = np.array([picked_color], dtype=np.uint8).reshape(1, 1, 3)
    picked_color_lab = cv2.cvtColor(picked_color_rgb, cv2.COLOR_RGB2Lab)[0][0]
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    delta_es = np.apply_along_axis(lambda lab_color: deltaE_cie76(picked_color_lab, lab_color), 2, lab_image)
    mask = delta_es < threshold
    result_image = image.copy()
    result_image[mask] = [0, 255, 0]  # Highlight in green
    return result_image

def main(image_path, threshold):
    global picked_color
    pick_color_from_image(image_path)
    similar_colors_image = find_similar_colors_in_image(image, picked_color, threshold)
    cv2.imshow("Similar Colors Highlighted", similar_colors_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find and highlight similar colors in an image.')
    parser.add_argument('image_path', type=str, help='Path to the input image file')
    parser.add_argument('--threshold', type=int, default=50, help='Threshold for color similarity. Default is 50.')
    args = parser.parse_args()

    picked_color = []
    main(args.image_path, args.threshold)
