class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.storage.get(key) is None:
            self.storage[key] = []
        self.storage[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage.get(key,[])
        result = ""
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] < timestamp: 
                result = values[mid][1] # best candidate we can find currently
                left = mid + 1
            elif values[mid][0] > timestamp:
                right = mid - 1
            else: 
                return values[mid][1] # direct hit
        # alternative we can return values[right][1] if right >= 0 else "", and save time setting the result value, but it's unintuitive for me
        return result

    #  basically just a worse binary search implementation, also before that I use dict[key,dict[timestamp,value]]
    def get_MySolution(self, key: str, timestamp: int) -> str:
        time_data = self.storage.get(key) 
        result = ""
        if time_data is None:
            return result
        
        time_keys = list(time_data.keys())
        left,right = 0, len(time_keys)-1

        while (left < right):
            middle_index = (left + right) // 2
            middle_value = time_keys[middle_index]
            if middle_value > timestamp:
                right = middle_index - 1
            elif middle_value < timestamp:
                left = middle_index + 1
            elif middle_value == timestamp:
                return time_data[time_keys[middle_index]]
            
        if time_keys[right] > timestamp:
            if right - 1 < 0:
                return ""
            return time_data[time_keys[right-1]]
        
        return time_data[time_keys[right]]
obj = TimeMap()

obj.set("A", "B", 5)
obj.set("A", "BB", 8)
obj.set("A", "BBB", 11)

print(obj.get("A", 4))  # ""
print(obj.get("A", 5))  # "B"
print(obj.get("A", 7))  # "B"
print(obj.get("A", 8))  # "BB"
print(obj.get("A", 9))  # "BB"
print(obj.get("A", 10))  # "BB"
print(obj.get("A", 11))  # "BBB"
print(obj.get("A", 12))  # "BBB"
