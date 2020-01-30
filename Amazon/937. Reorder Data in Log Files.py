class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        number = []
        for log in logs:
            split_log = log.split(' ')

            if split_log[1].isalpha(): 
                letter.append(( ' '.join(split_log[1:]), split_log[0]))
            else:
                number.append(log)
        letter.sort()
        return [ele[1]+ ' ' + ele[0] for ele in letter] + number
        
