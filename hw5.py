import cv2
import numpy as np
import heapq
from collections import deque

def load_image(filepath):
    image = cv2.imread(filepath)
    if image is None:
        print(f"Error loading image from {filepath}")
    else:
        print(f"Loaded image with shape: {image.shape}")
    return image

def save_image(image, filepath):
    cv2.imwrite(filepath, image)
    print(f"Image saved to {filepath}")

def is_valid_move(image, x, y, dx, dy, size=20):
    new_x = x + dx
    new_y = y + dy
    if new_x < 0 or new_y < 0 or new_x > image.shape[1] - 1 or new_y > image.shape[0] - 1:
        return False
    if dx == 0:
        if np.array_equal(image[y + dy//2, x], [255, 255, 255]):
            return False
    elif dy == 0:
        if np.array_equal(image[y, x + dx//2], [255, 255, 255]):
            return False
    return True

def dijkstra(image, start_x, start_y, end_x, end_y, size=20):
    # 設置優先隊列
    heap = []
    heapq.heappush(heap, (0, start_x, start_y))
    visited = set()
    distances = {}
    distances[(start_x, start_y)] = 0
    path = {}

    while heap:
        current_distance, x, y = heapq.heappop(heap)
        if (x, y) == (end_x, end_y):
            break
        visited.add((x, y))
        for dx, dy in [(-size, 0), (size, 0), (0, -size), (0, size)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(image, x, y, dx, dy, size) and (nx, ny) not in visited:
                new_distance = current_distance + 1
                if (nx, ny) not in distances or new_distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_distance
                    heapq.heappush(heap, (new_distance, nx, ny))
                    path[(nx, ny)] = (x, y)

    if (end_x, end_y) not in path:
        return []

    # 回溯路徑
    result_path = []
    step = (end_x, end_y)
    while step != (start_x, start_y):
        result_path.append(step)
        step = path[step]
    result_path.append((start_x, start_y))
    return result_path[::-1]

def draw_path(image, path, size=20):
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 4)

def main(input_image_path, output_image_path):
    image = load_image(input_image_path)
    if image is None:
        return
    start = (9, 9)
    end = (489, 489)
    path = dijkstra(image, start[0], start[1], end[0], end[1])
    if path:
        print("Path found:", path)
        draw_path(image, path)
        save_image(image, output_image_path)
    else:
        print("No path found")

if __name__ == "__main__":
    input_image_path = "maze4.bmp"
    output_image_path = "output_image.png"
    main(input_image_path, output_image_path)