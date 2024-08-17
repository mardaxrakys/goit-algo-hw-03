import os
import shutil
import sys

def copy_files_recursively(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                # Якщо елемент є директорією, викликаємо функцію рекурсивно
                new_dest_dir = os.path.join(dest_dir, item)
                os.makedirs(new_dest_dir, exist_ok=True)
                copy_files_recursively(src_path, new_dest_dir)
            else:
                # Якщо елемент є файлом, визначаємо його розширення
                file_extension = os.path.splitext(item)[1].lstrip('.').lower() or 'no_extension'
                extension_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(extension_dir, exist_ok=True)
                dest_path = os.path.join(extension_dir, item)
                
                # Копіюємо файл до відповідної піддиректорії
                shutil.copy2(src_path, dest_path)
                print(f"Копіювання: {src_path} -> {dest_path}")
    except Exception as e:
        print(f"Помилка при обробці {src_dir}: {e}")

def main():
    # Парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python script.py <src_dir> [<dest_dir>]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    # Перевірка наявності вихідної директорії
    if not os.path.exists(src_dir) or not os.path.isdir(src_dir):
        print(f"Директорія {src_dir} не існує або не є директорією.")
        sys.exit(1)

    # Створення директорії призначення
    os.makedirs(dest_dir, exist_ok=True)

    # Рекурсивне копіювання файлів
    copy_files_recursively(src_dir, dest_dir)

if __name__ == "__main__":
    main()
