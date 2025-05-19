import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    if "docs.google.com" in doc_url and "/edit" in doc_url:
        export_url = doc_url.replace("/edit", "/export?format=txt")
    else:
        raise ValueError("Error with replace url")

    # fetch content
    response = requests.get(export_url)
    if response.status_code != 200:
        raise Exception("Error request")

    text = response.text

    # parse
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    entries = []

    i = 3
    while i + 2 < len(lines):
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])
            entries.append((x, y, char))
            i += 3
        except:
            i += 1  # Skip in case of bad formatting

    if not entries:
        print("No valid character entries found.")
        return

    max_x = max(x for x, y, c in entries)
    max_y = max(y for x, y, c in entries)


    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in entries:
        grid[y][x] = char

    # print
    for row in grid:
        print("".join(row))

# Your input data: (x, character, y)
data = [
    (93, '░', 5), (2, '░', 5), (8, '░', 0), (39, '█', 1), (64, '░', 0),
    (63, '█', 1), (84, '█', 3), (9, '█', 4), (55, '█', 1), (23, '█', 4),
    (91, '█', 5), (21, '█', 5), (79, '░', 1), (65, '░', 1), (52, '█', 5),
    (49, '░', 5), (24, '░', 1), (42, '░', 5), (6, '█', 3), (24, '░', 2),
    (0, '█', 4), (65, '█', 3), (74, '░', 5), (36, '░', 6), (22, '█', 1),
    (62, '░', 3), (24, '░', 5), (58, '█', 5), (35, '█', 6), (55, '░', 3),
    (20, '█', 0), (88, '█', 3), (46, '█', 6), (8, '█', 5), (13, '█', 1),
    (76, '█', 4), (54, '█', 1), (2, '█', 0), (91, '█', 4), (34, '█', 6),
    (80, '█', 0), (12, '█', 5), (14, '░', 3), (1, '█', 2), (67, '░', 5),
    (93, '░', 1), (48, '█', 5), (79, '█', 0), (13, '█', 5), (39, '█', 5),
    (48, '░', 6), (12, '█', 3), (92, '█', 5), (52, '█', 4), (55, '░', 2),
    (61, '░', 5), (66, '█', 4), (7, '█', 6), (83, '█', 4), (33, '█', 0),
    (85, '░', 2), (56, '░', 0), (32, '█', 6), (72, '█', 5), (23, '█', 1),
    (40, '░', 3), (1, '█', 6), (28, '█', 0), (61, '█', 2), (19, '█', 6),
    (63, '█', 2), (41, '░', 2), (77, '░', 3), (57, '█', 3), (26, '█', 4),
    (38, '█', 3), (74, '█', 3), (84, '█', 4), (19, '█', 0), (9, '█', 1),
    (39, '█', 2), (1, '█', 3), (60, '█', 3), (28, '░', 2), (26, '█', 1),
    (14, '█', 0), (23, '█', 5), (30, '█', 6), (18, '█', 0), (53, '█', 2),
    (17, '█', 6), (4, '█', 0), (78, '░', 4), (29, '█', 6), (0, '█', 5),
    (22, '█', 2), (59, '█', 4), (85, '░', 1), (2, '░', 1), (77, '█', 4),
    (53, '█', 1), (67, '█', 6), (81, '░', 6), (47, '█', 5), (22, '░', 0),
    (5, '█', 0), (76, '█', 3), (43, '█', 0), (8, '█', 2), (1, '█', 4),
    (60, '█', 2), (32, '█', 0), (27, '█', 5), (15, '█', 0), (0, '█', 6),
    (41, '░', 4), (85, '░', 5), (84, '█', 1), (41, '█', 6), (62, '█', 1),
    (63, '█', 0), (92, '█', 2), (84, '█', 2), (42, '█', 0), (77, '█', 5),
    (43, '█', 6), (66, '█', 5), (15, '█', 6), (28, '░', 1), (91, '█', 0),
    (54, '█', 3), (71, '█', 0), (2, '█', 3), (29, '█', 3), (73, '░', 0),
    (84, '█', 5), (83, '█', 6), (6, '█', 0), (8, '█', 1), (26, '█', 1),
]

# Find max coordinates to size the grid
max_x = max(point[0] for point in data)
max_y = max(point[2] for point in data)

# Create blank grid initialized with spaces
grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# Place characters in grid
for x, char, y in data:
    grid[y][x] = char

# Print the grid line by line
for row in grid:
    print(''.join(row))

def main():
    print("hello")
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    decode_secret_message(url)
    print("Success")

if __name__ == "__main__":
    main()