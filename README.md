# jsonapi

This jsonapi extends the functionality of the built-in `json` library by providing custom serialization and deserialization for complex numbers and range objects.

## Installation

You can install this library using `pip install jsonapi`:


## Run Test

python -m unittest test_jsonap

## Code Examples

Example 1: Serialization and Deserialization of Complex Numbers:
import jsonapi

### Create a complex number
my_complex = complex(2.5, 3.7)

### Serialize the complex number to JSON
json_data = jsonapi.dumps(my_complex)

### Deserialize JSON back to a complex number
deserialized_complex = jsonapi.loads(json_data)

print("Original Complex Number:", my_complex)
print("Deserialized Complex Number:", deserialized_complex)

Example 2: Serialization and Deserialization of Range Objects:
import jsonapi

### Create a range object
my_range = range(1, 10, 2)

### Serialize the range object to JSON
json_data = jsonapi.dumps(my_range)

### Deserialize JSON back to a range object
deserialized_range = jsonapi.loads(json_data)

print("Original Range Object:", list(my_range))
print("Deserialized Range Object:", list(deserialized_range))
