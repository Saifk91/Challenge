## Assumptions:
# 1) the key value will always be an alphabet and number and no other special character
# 2) The delimiter can be any special character
# 3) the result will be an object in cases when nested values in object are greater than sub key's in key
# 4) the result will be "Invalid Key" in cases when nested values in object are lesser than sub key's in key
import json

def get_value(object, key):
    if not object or not key:
        return None

    if isinstance(object, str):
        object = json.loads(object)

    key_len = len(key)
    curr_object = object

    for i in range(0, key_len):
        curr_sub_key = key[i]
        if curr_sub_key.isalpha() or curr_sub_key.isnumeric():
            if isinstance(curr_object, dict):
                if curr_object.get(curr_sub_key):
                    curr_object = curr_object.get(curr_sub_key)
                else:
                    return "Key not present"
            elif isinstance(curr_object, str):
                return "Invalid Key"
            else:
                return f"Invalid data type in object: {type(curr_object)}"
        else:
            continue

    return curr_object


### Test cases
##positive case 1
print(f'positive case 1: {get_value({"a":{"b":{"c":"d"}}}, "a/b/c")}')
##positive case 2
print(f'positive case 2: {get_value({"a":{"b":{"c":{"d":"e"}}}}, "a/b/c/d")}')
##when key has numeric value as well
print(f'when key has numeric value as well: {get_value({"a":{"b":{"c":{"1":"e"}}}}, "a/b/c/1")}')
##when object is a string
object = '{"a":{"b":{"c":"d"}}}'
print(f'when object is a string: {get_value(object, "a%b%c")}')
##when object is null
print(f'when object is null: {get_value(None, "a/b/c")}')
##when key is null
print(f'when key is null: {get_value({"a":{"b":{"c":"d"}}}, None)}')
##when delimiter is other than "/"
print(f'when delimiter is other than "/": {get_value({"a":{"b":{"c":"d"}}}, "a%b%c")}')
##when delimiter is a combination of special characters
print(f'when delimiter is a combination of special characters: {get_value({"a":{"b":{"c":"d"}}}, "a%b|c")}')
##when key has less sub keys than object's nested values
print(f'when key has less sub keys than objects nested values: {get_value({"a":{"b":{"c":"d"}}}, "a%b")}')
##when key has more sub keys than object's nested values
print(f'when key has more sub keys than objects nested values: {get_value({"a":{"b":{"c":"d"}}}, "a%b%c%e")}')