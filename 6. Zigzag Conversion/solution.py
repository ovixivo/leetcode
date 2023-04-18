class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []

        for i in range(numRows):
            arr.append([])

        counter = 0
        row = 0
        column = 0
        i = 0
        while (i < len(s)):
            row = 0
            if counter <= 0:
                counter = 0
                while counter < numRows:
                    if i >= len(s):
                        break
                    arr[row].append(s[i])
                    counter += 1
                    i += 1 
                    row += 1
                counter -= 1
            else:
                for j in range(numRows):
                    arr[j].append('')     
                arr[counter][column] = s[i]
                i += 1
            
            column += 1
            counter -= 1
            
        answer_arr = []
        for item in arr:
            answer_arr.append("".join(item))

        return "".join(answer_arr)
