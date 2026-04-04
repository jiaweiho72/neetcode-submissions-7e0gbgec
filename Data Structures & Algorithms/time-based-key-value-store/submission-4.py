class TimeMap:
    """
    5 Apr 2026
    - store multiple values for same key at diff timestamps
    - retrieve key's value at timestamp

    - return the most recent val where prev timetamp <= input timestamp
        - else return ''
    - you still are searching for something -> BS
        - max timestamp <= input timestamp

    idea
    - data structure
        - timestamp list of tuple, sorted by timestamp
            - already sorted as input are in choronological order

    - BS to find key == key and timestamp the max but less thaan input time


    Mistake
    - does not work if you just have a timestamp list with no keyvalue store. 
    when you binary search, you won't be able to determine direction if value is not k
    solution
    - a list of timestamps per key
    """
    def __init__(self):
        self.kv_store = {}       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key] = self.kv_store.get(key, [])
        self.kv_store[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store: # handle key not inside
            return ""
        timestamps = self.kv_store[key]
        n = len(timestamps)
        l, r = 0, n - 1
        most_recent_val = ""
        while l <= r:
            m = (l + r) // 2
            t, v = timestamps[m]
            if t <= timestamp: # valid but find more recent -> shift right
                most_recent_val = v # just update overwrite as it will be most recent
                l = m + 1
            else: # t > timestamp: # shift left
                r = m - 1
                
            
        return most_recent_val







        
