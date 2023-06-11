# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 
# Constraints:

# 1 <= length <= 5 * 104
# 0 <= index < length
# 0 <= val <= 109
# 0 <= snap_id < (the total number of times we call snap())
# At most 5 * 104 calls will be made to set, snap, and get.






class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]
        self.current_snap_id = 0        

    def set(self, index: int, value: int) -> None:
        snap = self.array[index][-1]
        if snap[0] == self.current_snap_id:
            snap[1] = value
        else:
            self.array[index].append([self.current_snap_id, value])

    def snap(self) -> int:
        self.current_snap_id += 1
        return self.current_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshot_index = bisect_left(self.array[index], [snap_id + 1]) - 1
        return self.array[index][snapshot_index][1]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)



