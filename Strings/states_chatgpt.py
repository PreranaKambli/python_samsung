import sys

# Check if command-line arguments are passed
if len(sys.argv) < 2:
    print("Please provide at least one state-capital pair as an argument.")
    sys.exit()

# Initialize two lists for states and capitals
states = []
capitals = []

# Iterate through each command-line argument (excluding the script name)
for arg in sys.argv[1:]:
    parts = arg.split(' ', 1)  # Split each string into two parts: state and capital
    if len(parts) == 2:
        state, capital = parts
        states.append(state)
        capitals.append(capital)
    else:
        print(f"Invalid input: '{arg}', must contain both state and capital separated by space.")
        continue

# Print the state and capital in table format
print(f"{'State':<20} {'Capital':<20}")
print("="*40)  # A separator line

# Print each state-capital pair in a formatted manner
for state, capital in zip(states, capitals):
    print(f"{state:<20} {capital:<20}")
