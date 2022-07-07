import os
import sys
import cv2
import numpy as np

skip_rate = 100
movie_path = 'movie.mp4'


def calc_avg_color(img):
    avg_color = [0, 0, 0]
    for i in img:
        for pixel in i:
            avg_color[0] += pixel[0]
            avg_color[1] += pixel[1]
            avg_color[2] += pixel[2]
    avg_color[0] = round(avg_color[0] / (len(img) * len(img[0])))
    avg_color[1] = round(avg_color[1] / (len(img) * len(img[0])))
    avg_color[2] = round(avg_color[2] / (len(img) * len(img[0])))
    return avg_color


if len(sys.argv) >= 2:
    movie_path = sys.argv[1]
if len(sys.argv) == 3:
    skip_rate = int(sys.argv[2])

vidcap = cv2.VideoCapture(movie_path)
success, image = vidcap.read()
colors = []
total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
progress = 0

if not success:
    print('ERROR: Could not read video file', file=sys.stderr)
    sys.exit(1)

while success:
    frame_color = calc_avg_color(image)
    colors.append(frame_color)
    progress += skip_rate
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, progress)
    success, image = vidcap.read()
    print("{:.2f}".format((progress - skip_rate) / total_frames * 100), "%")

width = total_frames // 2 // skip_rate + 1
final_image = np.zeros((width, total_frames // skip_rate + 1, 3), dtype=np.uint8)
i = 0
for color in colors:
    for j in range(width):
        final_image[j][i] = color
    i += 1

movie_name = os.path.splitext(os.path.basename(movie_path))[0]
cv2.imwrite('color_of_' + movie_name + '_' + str(skip_rate) + '.jpg', final_image)
