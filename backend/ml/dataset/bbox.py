def normalize_bbox(bbox, width, height):
    xs = [point[0] for point in bbox]

    ys = [point[1] for point in bbox]

    x0 = max(0, min(xs))

    y0 = max(0, min(ys))

    x1 = min(width, max(xs))

    y1 = min(height, max(ys))

    return [
        int(1000 * x0 / width),
        int(1000 * y0 / height),
        int(1000 * x1 / width),
        int(1000 * y1 / height),
    ]