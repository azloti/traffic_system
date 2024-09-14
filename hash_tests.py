from hash_table import HashTable

def test_hash_table():
    # Create a hash table of size 5
    table = HashTable(5)

    # Try to search for a key that doesn't exist
    assert table.search("hello") == None

    # Insert some values
    table.insert("hello", "world")
    table.insert("foo", "bar")
    table.insert("cat", "dog")

    # Search for values
    assert table.search("hello") == "world"
    assert table.search("foo") == "bar"
    assert table.search("cat") == "dog"

    # Delete values
    table.delete("hello")
    table.delete("foo")
    table.delete("cat")

    # Check that the values were deleted
    assert table.search("hello") == None
    assert table.search("foo") == None
    assert table.search("cat") == None

    print("All hash tests pass")