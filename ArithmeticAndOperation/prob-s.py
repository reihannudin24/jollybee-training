import math


def main():
    # Input: panjang prisma L, panjang sisi segitiga B, dan tinggi segitiga H
    L, B, H = map(float, input().split())

    # Menghitung luas alas segitiga
    area_base = (math.sqrt(3) / 4) * (B ** 2)

    # Menghitung luas sisi tegak
    area_side = 3 * (B * L)

    # Menghitung luas permukaan total
    surface_area = 2 * area_base + area_side

    # Output luas permukaan, dibulatkan hingga 3 angka di belakang koma
    print(f"{surface_area:.3f}")


if __name__ == '__main__':
    main()
