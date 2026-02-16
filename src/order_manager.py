def validate_kitchen_size(width, height):
    if width < 150 or width > 500:
        return False, "Ширина должна быть от 150 до 500 см"
    if height < 200 or height > 300:
        return False, "Высота должна быть от 200 до 300 см"
    return True, "Размеры корректны"
if __name__ == "__main__":
    print(validate_kitchen_size(250, 220)
print('ПАРОЛЬ: admin123')
