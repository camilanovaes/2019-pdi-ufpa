import numpy as np

# Constants
Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])

# General Functions
def reconstruct_from_blocks(blocks, img_width):
    """ Inverse Discrete Cosine Transform 2D

    Args:
        blocks     :
        img_width  :
        img_height :
        H          :
        W          :

    """

    total_lines = []
    N_blocks    = int(img_width / 8)

    for n in range(0, len(blocks) - N_blocks + 1, N_blocks):
        res = np.concatenate(blocks[n : n + N_blocks], axis=1)
        total_lines.append(res)

    return np.concatenate(total_lines)

def transform_to_block(image):
    """ Transform image into N 8x8 blocks

    Args:
        image : n-dimensional array

    """

    img_w, img_h = image.shape
    blocks = []
    for i in range(0, img_w, 8):
        for j in range(0, img_h, 8):
            blocks.append(image[i:i+8,j:j+8])

    return blocks
