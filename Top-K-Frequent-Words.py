class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        bucket = defaultdict(list)
        for w, cnt in counter.items():
            bucket[cnt].append(w)
        
        #get the sorted bucket frequency
        for freq in bucket:
            bucket[freq].sort()

        res = []
        # start from max frequency to 0
        for freq in range(max(bucket.keys()), -1, -1):
            if freq in bucket:
                for word in bucket[freq]:
                    res.append(word)
                    if len(res) == k:
                        return res
        return res
                
           
        