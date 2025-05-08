class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) #create count hashmap
        bucket = defaultdict(list) # list ->dict
        for char, cnt in count.items():
            bucket[cnt].append(char)
        res = []
        print(bucket)
        for i in range(len(s) , -1, -1):
            for c in bucket[i]:
                res.append(c*i)
        return \\.join(res)
        