from matplotlib import pyplot as plt

class BaseFuzzy():
    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)

class Speed(BaseFuzzy):
    def __init__(self):
        self.p1 = 0
        self.p2 = 40
        self.pn = 80

    def slow(self, x):
        if x >= self.p2:
            return 0
        elif x <= self.p1:
            return 1
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.down(x)

    def steady(self, x):
        if x >= self.p2 or x <= self.p1:
            return 0
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)

    def fast(self, x):
        if x <= self.p1:
            return 0
        elif x >= self.p2:
            return 1
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)

    def graph(self, ax, value=None):
        x = [0, self.p1, self.p2, self.pn]
        y_slow = [1, 1, 0, 0]
        ax.plot(x, y_slow, label='slow', color='C0')
        y_steady = [0, 0, 1, 1]
        ax.plot(x, y_steady, label='steady', color='C1')
        y_fast = [0, 0, 1, 1]
        ax.plot(x, y_fast, label='fast', color='C2')
        ax.set_title('Speed')
        ax.legend(loc='upper left')
        if value:
            x_param = [0, value, value]
            slow_value = self.slow(value)
            y_param_slow = [slow_value, slow_value, 0]
            ax.plot(x_param, y_param_slow, 'o--', color='C0')
            steady_value = self.steady(value)
            y_param_steady = [steady_value, steady_value, 0]
            ax.plot(x_param, y_param_steady, 'o--', color='C1')
            fast_value = self.fast(value)
            y_param_fast = [fast_value, fast_value, 0]
            ax.plot(x_param, y_param_fast, 'o--', color='C2')


class Pressure(BaseFuzzy):
    def __init__(self):
        self.p1 = 0
        self.p2 = 30
        self.pn = 60

    def very_low(self, x):
        if x >= self.p2:
            return 0
        elif x <= self.p1:
            return 1
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.down(x)

    def low(self, x):
        if x >= self.p2 or x <= self.p1:
            return 0
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)

    def medium(self, x):
        if x <= self.p1:
            return 0
        elif x >= self.p2:
            return 1
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)

    def high(self, x):
        if x <= self.p1:
            return 0
        elif x >= self.pn:
            return 1
        else:
            self.maximum = self.pn
            self.minimum = self.p1
            return self.up(x)

    def very_high(self, x):
        if x <= self.p1:
            return 0
        elif x >= self.pn:
            return 1
        else:
            self.maximum = self.pn
            self.minimum = self.p1
            return self.up(x)

    def graph(self, ax, value=None):
        x = [0, self.p1, self.p2, self.pn]
        y_very_low = [1, 1, 0, 0]
        ax.plot(x, y_very_low, label='very_low', color='C0')
        y_low = [0, 0, 1, 1]
        ax.plot(x, y_low, label='low', color='C1')
        y_medium = [0, 0, 1, 1]
        ax.plot(x, y_medium, label='medium', color='C2')
        y_high = [0, 0, 1, 1]
        ax.plot(x, y_high, label='high', color='C3')
        y_very_high = [0, 0, 1, 1]
        ax.plot(x, y_very_high, label='very_high', color='C4')
        ax.set_title('Pressure')
        ax.legend(loc='upper left')
        if value:
            x_param = [0, value, value]
            very_low_value = self.very_low(value)
            y_param_very_low = [very_low_value, very_low_value, 0]
            ax.plot(x_param, y_param_very_low, 'o--', color='C0')
            low_value = self.low(value)
            y_param_low = [low_value, low_value, 0]
            ax.plot(x_param, y_param_low, 'o--', color='C1')
            medium_value = self.medium(value)
            y_param_medium = [medium_value, medium_value, 0]
            ax.plot(x_param, y_param_medium, 'o--', color='C2')
            high_value = self.high(value)
            y_param_high = [high_value, high_value, 0]
            ax.plot(x_param, y_param_high, 'o--', color='C3')
            very_high_value = self.very_high(value)
            y_param_very_high = [very_high_value, very_high_value, 0]
            ax.plot(x_param, y_param_very_high, 'o--', color='C4')


class Temperature(BaseFuzzy):
    def __init__(self):
        self.p1 = 0
        self.p2 = 30
        self.pn = 60

    def hot(self, x):
        if x >= self.p2:
            return 1
        elif x <= self.p1:
            return 0
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)

    def warm(self, x):
        if x >= self.p2 or x <= self.p1:
            return 0
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)

    def cold(self, x):
        if x <= self.p1:
            return 1
        elif x >= self.p2 and x <= self.pn:
            return 0
        else:
            self.maximum = self.pn
            self.minimum = self.p2
            return self.down(x)

    def freeze(self, x):
        if x <= self.p2:
            return 0
        elif x >= self.pn:
            return 1
        else:
            self.maximum = self.pn
            self.minimum = self.p2
            return self.up(x)

    def graph(self, ax, value=None):
        x = [0, self.p1, self.p2, self.pn]
        y_hot = [0, 0, 1, 1]
        ax.plot(x, y_hot, label='hot', color='C0')
        y_warm = [0, 0, 1, 1]
        ax.plot(x, y_warm, label='warm', color='C1')
        y_cold = [1, 1, 0, 0]
        ax.plot(x, y_cold, label='cold', color='C2')
        y_freeze = [0, 0, 1, 1]
        ax.plot(x, y_freeze, label='freeze', color='C3')
        ax.set_title('Temperature')
        ax.legend(loc='upper left')
        if value:
            x_param = [0, value, value]
            hot_value = self.hot(value)
            y_param_hot = [hot_value, hot_value, 0]
            ax.plot(x_param, y_param_hot, 'o--', color='C0')
            warm_value = self.warm(value)
            y_param_warm = [warm_value, warm_value, 0]
            ax.plot(x_param, y_param_warm, 'o--', color='C1')
            cold_value = self.cold(value)
            y_param_cold = [cold_value, cold_value, 0]
            ax.plot(x_param, y_param_cold, 'o--', color='C2')
            freeze_value = self.freeze(value)
            y_param_freeze = [freeze_value, freeze_value, 0]
            ax.plot(x_param, y_param_freeze, 'o--', color='C3')


class FuzzyInferenceSystem():
    def __init__(self, speed, pressure, temperature):
        self.speed = speed
        self.pressure = pressure
        self.temperature = temperature

    def get_membership_values(self, speed_value, pressure_value):
        speed_slow = self.speed.slow(speed_value)
        speed_steady = self.speed.steady(speed_value)
        speed_fast = self.speed.fast(speed_value)

        pressure_very_low = self.pressure.very_low(pressure_value)
        pressure_low = self.pressure.low(pressure_value)
        pressure_medium = self.pressure.medium(pressure_value)
        pressure_high = self.pressure.high(pressure_value)
        pressure_very_high = self.pressure.very_high(pressure_value)

        return {
            'speed_slow': speed_slow,
            'speed_steady': speed_steady,
            'speed_fast': speed_fast,
            'pressure_very_low': pressure_very_low,
            'pressure_low': pressure_low,
            'pressure_medium': pressure_medium,
            'pressure_high': pressure_high,
            'pressure_very_high': pressure_very_high
        }

    def infer(self, speed_value, pressure_value):
        membership_values = self.get_membership_values(speed_value, pressure_value)

        temperature_hot = min(membership_values['speed_slow'], membership_values['pressure_very_low'])
        temperature_warm = max(membership_values['speed_steady'], membership_values['pressure_low'], membership_values['speed_fast'], membership_values['pressure_medium'])
        temperature_cold = membership_values['pressure_high']
        temperature_freeze = min(membership_values['speed_slow'], membership_values['pressure_very_high'], membership_values['speed_steady'], membership_values['speed_fast'])

        return {
            'temperature_hot': temperature_hot,
            'temperature_warm': temperature_warm,
            'temperature_cold': temperature_cold,
            'temperature_freeze': temperature_freeze
        }

    def defuzzify(self, inference_result):
        numerator = (inference_result['temperature_hot'] * self.temperature.p2) + (inference_result['temperature_warm'] * self.temperature.p2) + (inference_result['temperature_cold'] * self.temperature.p1) + (inference_result['temperature_freeze'] * self.temperature.pn)
        denominator = inference_result['temperature_hot'] + inference_result['temperature_warm'] + inference_result['temperature_cold'] + inference_result['temperature_freeze']
        if denominator != 0:
            return numerator / denominator
        else:
            return 0

    def visualize(self, speed_value, pressure_value, temperature_value):
        fig, axes = plt.subplots(3, figsize=(8, 12))

        self.speed.graph(axes[0], speed_value)
        self.pressure.graph(axes[1], pressure_value)
        self.temperature.graph(axes[2], temperature_value)

        plt.tight_layout()
        plt.show()


# Inisialisasi variabel fuzzy
speed = Speed()
pressure = Pressure()
temperature = Temperature()

# Inisialisasi sistem inferensi fuzzy
fuzzy_system = FuzzyInferenceSystem(speed, pressure, temperature)

# Input
print(' ----------------------------------------------')
print('|            HAMIDAN MAKSUM NUR HIDAYAT        |')
print('|                  201011401510                |')
print('|              UAS KECERDASAN BUATAN           |')
print(' ----------------------------------------------')
print('\nSILAHKAN INPUT NILAI SPEED & PRESSURE ')
speed_value = float(input("\nMasukkan nilai Speed: "))
pressure_value = float(input("Masukkan nilai Pressure: "))

inference_result = fuzzy_system.infer(speed_value, pressure_value)
temperature_value = fuzzy_system.defuzzify(inference_result)

print('\nSpeed:', speed_value)
print('Pressure:', pressure_value)
print()
print('Hasilnya :')
print('Temperature Hot:', inference_result['temperature_hot'])
print('Temperature Warm:', inference_result['temperature_warm'])
print('Temperature Cold:', inference_result['temperature_cold'])
print('Temperature Freeze:', inference_result['temperature_freeze'])
print()
print('Defuzzified Temperature:', temperature_value)

# Visualisasi
fuzzy_system.visualize(speed_value, pressure_value, temperature_value)