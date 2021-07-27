import math

def takeoff():
    a = float(input("Enter Acceleration Rate: "))
    s = float(input("Enter takeoff speed: "))
    l = math.ceil((s**2) / (2*a))
    print(f"Runway Length of {l} meters needed for Takeoff Speed of {s} and Acceleration of {a}")

takeoff()