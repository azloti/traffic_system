from city import City
import random

def test_city():
    # Create a city
    city = City()

    # Add edges
    city.add_edge("A", "C", 1)
    city.add_edge("C", "B", 2)
    city.add_edge("B", "D", 3)

    # Find a path from A to D
    assert city.find_shortest_path("A", "D") == ['A', 'C', 'B', 'D']

    # Edge case: Find a path from A to A
    assert city.find_shortest_path("A", "A") == ['A']

    # Edge case: Find a path from A to X
    assert city.find_shortest_path("A", "X") == None

    # Add more edges
    city.add_edge("D", "E", 4)
    city.add_edge("A", "E", 5)

    # Find a path from A to E
    assert city.find_shortest_path("A", "E") == ['A', 'E']

    # Add a random edge
    city.add_edge("N", "O", 6)

    # Find a path from A to O
    assert city.find_shortest_path("A", "O") == None

    print("All city tests pass")

def test_city_stress_testing():

    # Create a city
    city = City()


    # Add 1 million of random edges
    for i in range(1000000):
        # random weight
        weight = random.randint(1, 100)

        # Random target node, between 1 and 100 nodes away
        targetDiff = random.randint(1, 100)

        city.add_edge(str(i), str(i + targetDiff), weight)

    print ("1 million edges added")

    # Time how long it takes to find a path from 0 to 100
    import time
    start = time.time()
    city.find_shortest_path("0", "10000")
    end = time.time()

    print(f"Time taken: {end - start} seconds")

    # Assert that the time taken is less than 0.5 seconds
    assert end - start < 0.5

    print("All city stress tests pass")

test_city_stress_testing()