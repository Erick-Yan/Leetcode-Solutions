'''
    My Solution: Create a dictionary to track all unique anagrams in the list. 
    Iterate through the list and append each element into the dictionary key, which is the alphabetically sorted element.
    Return the dictionary values.

    Learned: dictionary.get(dictionary_key, value_if_key_value_empty)
'''

class Solution(object):
    def groupAnagrams(self, strs):
        sims_dict = dict()
        for stir in strs:
            stir_mod = "".join(sorted(stir))
            sims_dict[stir_mod] = sims_dict.get(stir_mod, []) + [stir]
            
        return sims_dict.values()