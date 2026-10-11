class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s = "racecar", t = "carrace"
        if len(s) != len(t):
            return False
        counts, countt = Counter(s), Counter(t)
        for key, value in counts.items():
            if key not in countt or countt[key] != value:
                return False
        return True
        
            
        
        


        