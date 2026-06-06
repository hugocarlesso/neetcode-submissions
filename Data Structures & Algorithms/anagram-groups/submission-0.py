class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_occs = {}
        result = []
        # need to match result index as the key of the dict_occs
        for string in strs:
            dict_occ = {}
            for car in string:
                dict_occ[car] = dict_occ.get(car, 0) +1
            if dict_occ in dict_occs.values():
                index = list(dict_occs.keys())[list(dict_occs.values()).index(dict_occ)]
                result[index].append(string)
            else:
                dict_occs[len(result)] = dict_occ
                result.append([string])
        return result