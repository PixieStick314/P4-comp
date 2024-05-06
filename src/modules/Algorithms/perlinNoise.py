# perlinNoise.py
import numpy as np
import noise

def apply_perlin_noise(array, scale, octaves, persistence, lacunarity):
    num_rows = len(array)
    num_cols = len(array[0]) if num_rows > 0 else 0
    for i in range(num_rows[0]):
        for j in range(num_cols[1]):
            array[i][j] = noise.pnoise2(i / scale, j / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

    return array