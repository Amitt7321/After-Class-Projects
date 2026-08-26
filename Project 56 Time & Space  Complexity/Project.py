n = 5

print("================================")
print("MY RUNNING LAP TRACKER")
print("================================")
print("Number of laps:", n)
print()

formula_total = n * (n + 1) // 2

print("Solution 1: Formula Method")
print("Total Running Points:", formula_total)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()

loop_total = 0
steps_loop = 0

for lap in range(1, n + 1):
    loop_total = loop_total + lap
    steps_loop = steps_loop + 1

print("Solution 2: Loop Method")
print("Total Running Points:", loop_total)
print("Steps Taken:", steps_loop)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()

nested_total = 0
steps_nested = 0

for lap in range(1, n + 1):
    for point in range(1, lap + 1):
        nested_total = nested_total + 1
        steps_nested = steps_nested + 1

print("Solution 3: Nested Loop Method")
print("Total Running Points:", nested_total)
print("Steps Taken:", steps_nested)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()

print("================================")
print("ALGORITHM EFFICIENCY COMPARISON")
print("================================")
print("Formula Method: Fastest because it uses only 1 calculation.")
print("Loop Method: Slower because it repeats once for every lap.")
print("Nested Loop Method: Slowest because it uses a loop inside another loop.")
print()
print("Best Method: Formula Method")
print("Reason: It has O(1) time complexity, so it stays fast even when laps increase.")
print("================================")