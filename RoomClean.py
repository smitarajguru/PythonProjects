status_A = input("Enter status of location A (Clean/Dirty): ").capitalize()
status_B = input("Enter status of location B (Clean/Dirty): ").capitalize()

environment = {
    "A": status_A,
    "B": status_B
}

location = input("Enter starting location (A/B): ").upper()

steps = int(input("Enter the number of steps to run: "))

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"

print("\n--- Initial Environment ---")
print("Environment:", environment)
print("Starting Location:", location)

for i in range(steps):
    status = environment[location]
    action = vacuum_agent(location, status)

    print(f"\nStep {i + 1}")
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"

print("\n--- Final Environment ---")
print("Environment:", environment)
print("Final Location:", location)
