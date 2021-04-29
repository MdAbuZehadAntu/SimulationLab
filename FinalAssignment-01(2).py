class Reaction:
    kb = 0.02
    kf = 0.035
    threshold = 0.1
    time_step = 0.3

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def rate_a(self, a, b, c):
        return (self.kb * c) - (2 * self.kf * a * b)

    def rate_b(self, a, b, c):
        return (self.kb * c) - (1.6 * self.kf * a * b)

    def rate_c(self, a, b, c):
        return 3 * self.kf * a * b - (1.8 * self.kb * c)

    def simulate(self):
        temp_time = 0
        while True:
            temp_a = self.A
            temp_b = self.B
            temp_c = self.C
            temp_time += self.time_step

            self.A = self.A + self.rate_a(temp_a, temp_b, temp_c) * self.time_step
            self.B = self.B + self.rate_b(temp_a, temp_b, temp_c) * self.time_step
            self.C = self.C + self.rate_c(temp_a, temp_b, temp_c) * self.time_step
            print(f"At time = {round(temp_time, 1)} : ")
            print(f"C1 : {self.A}")
            print(f"C2 : {self.B}")
            print(f"C3 : {self.C}")
            print()

            if abs(self.A - temp_a) < self.threshold and abs(self.B - temp_b) < self.threshold and abs(
                    self.C - temp_c) < self.threshold:
                break


react = Reaction(50, 25, 20)
react.simulate()
