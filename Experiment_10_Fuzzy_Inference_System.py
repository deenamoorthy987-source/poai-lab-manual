"""
Experiment 10: Fuzzy Inference System
Example: Control fan speed using room temperature and humidity.

This is a small Mamdani-style fuzzy inference demonstration.
It uses triangular membership functions and weighted rule outputs.
No external Python packages are required.
"""

def triangular_membership(value, a, b, c):
    """Return the membership degree of value in triangular set (a, b, c)."""
    if value < a or value > c:
        return 0.0
    if value == b:
        return 1.0
    if value < b:
        return (value - a) / (b - a) if b != a else 1.0
    return (c - value) / (c - b) if c != b else 1.0


def temperature_memberships(temp):
    return {
        "low": triangular_membership(temp, 0, 18, 30),
        "medium": triangular_membership(temp, 20, 30, 40),
        "high": triangular_membership(temp, 30, 42, 50),
    }


def humidity_memberships(humidity):
    return {
        "low": triangular_membership(humidity, 0, 25, 50),
        "medium": triangular_membership(humidity, 30, 50, 70),
        "high": triangular_membership(humidity, 50, 75, 100),
    }


def fan_speed(temp, humidity):
    t = temperature_memberships(temp)
    h = humidity_memberships(humidity)

    # Rule base:
    # If temperature is low, fan speed is low.
    # If temperature is medium and humidity is low, speed is medium.
    # If temperature is medium and humidity is medium/high, speed is high.
    # If temperature is high, fan speed is high.
    rules = [
        (t["low"], 20),
        (min(t["medium"], h["low"]), 50),
        (min(t["medium"], h["medium"]), 75),
        (min(t["medium"], h["high"]), 85),
        (t["high"], 100),
    ]

    total_strength = sum(strength for strength, _ in rules)
    if total_strength == 0:
        return 0.0

    # Weighted-average defuzzification.
    output = sum(strength * speed for strength, speed in rules)
    return output / total_strength


def main():
    print("FUZZY INFERENCE SYSTEM - FAN SPEED CONTROL")
    try:
        temperature = float(input("Enter temperature (0 to 50 C): "))
        humidity = float(input("Enter humidity (0 to 100 %): "))

        if not 0 <= temperature <= 50:
            print("Temperature must be between 0 and 50.")
            return
        if not 0 <= humidity <= 100:
            print("Humidity must be between 0 and 100.")
            return

        speed = fan_speed(temperature, humidity)
        print(f"Recommended fan speed: {speed:.2f}%")

        if speed < 35:
            print("Fan speed category: LOW")
        elif speed < 70:
            print("Fan speed category: MEDIUM")
        else:
            print("Fan speed category: HIGH")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
