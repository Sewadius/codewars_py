def draw_stairs(n: int) -> str:
    return ''.join(
        (' ' * i + 'I\n') if i != n - 1 else (' ' * i + 'I') for i in range(n)
    )


print(draw_stairs(7))
