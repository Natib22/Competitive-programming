class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_map = {}
        
        for pt in points:
            dist = (pt[0] ** 2 + pt[1] ** 2) ** 0.5
            
            if dist in dist_map:
                dist_map[dist].append(pt)
            else:
                dist_map[dist] = [pt]
        
        sorted_dists = sorted(dist_map.keys())
        result = []
        
        for dist in sorted_dists:
            pts = dist_map[dist]
            
            for p in pts:
                if len(result) < k:
                    result.append(p)
                else:
                    break
            
            if len(result) >= k:
                break
        
        return result

