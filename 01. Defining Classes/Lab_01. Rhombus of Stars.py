def repeat_str(text, count_to_repeat):
    return ''.join([text for i in range(count_to_repeat)])


class Rhombus:
    def __init__(self, n):
        self.n = n

    def draw(self):
        upper_down_rows = n - 1

        for j in range(upper_down_rows + 1):
            print(repeat_str(" ", upper_down_rows - j) + repeat_str("* ", j + 1))

        for k in range(upper_down_rows - 1, -1, -1):
            print(repeat_str(" ", upper_down_rows - k) + repeat_str("* ", k + 1))


n = int(input())
rhombus = Rhombus(n)
rhombus.draw()