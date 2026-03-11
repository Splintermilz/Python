### --- COORD HUNTER --- ###

### Variables

coord_a = {
    "x": 450,
    "y": 320
}

coord_b = {
    "x": 543,
    "y": 282
}

coord_c = {
    "x": 512,
    "y": 210
}

coord_d = {
    "x": 183,
    "y": 293
}

coords = [coord_a, coord_b, coord_c, coord_d]


### Function

def get_highest(coords: list[dict]) -> dict:
    # Highest is the greatest y value
    highest = {
        "x": 0,
        "y": 0
    }

    for coord in coords:
        if coord["y"] > highest["y"]:
            highest = coord

    return highest


print(get_highest(coords))


def get_farthest(coords: list[dict]) -> dict:
    # Farthest is the greatest x value
    farthest = {
        "x": 0,
        "y": 0
    }

    for coord in coords:
        if coord["x"] > farthest["x"]:
            farthest = coord

    return farthest


print(get_farthest(coords))


def get_mid(coords: list[dict]) -> dict:
    total_x = 0
    total_y = 0

    for coord in coords:
        total_x += coord["x"]
        total_y += coord["y"]

    center = {
        "x": total_x / len(coords),
        "y": total_y / len(coords)
    }

    return center


print(get_mid(coords))

