import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def koch_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

def main():
    # Налаштування екрану
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Фрактал Сніжинка Коха")

    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Введення рівня рекурсії від користувача
    depth = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    
    # Малюємо сніжинку Коха
    koch_snowflake(t, 400, depth)
    
    # Завершення роботи
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
