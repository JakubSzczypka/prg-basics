print("SURVEY")
cs = input("Are you interested in computer science? (y/n): ") == 'y'
games = input("Do you like playing computer games? (y/n): ") == 'y'
ig = input("Do you have an Instagram account? (y/n): ") == 'y'
print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if cs else 'No'}")
print(f"Playing computer games: {'Yes' if games else 'No'}")
print(f"Has an Instagram account: {'Yes' if ig else 'No'}")
