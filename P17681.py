def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        bin_a1 = bin(arr1[i])
        bin_a1 = bin_a1[2:]
        while n > len(bin_a1):
            bin_a1 = "0" + bin_a1
        bin_a2 = bin(arr2[i])
        bin_a2 = bin_a2[2:]
        while n > len(bin_a2):
            bin_a2 = "0" + bin_a2
        bin_a1 = str(bin_a1)
        bin_a2 = str(bin_a2)
        st = ""
        print(bin_a1, bin_a2)
        for j in range(n):
            if bin_a1[j] == "1" or bin_a2[j] == "1":
                st += "#"
            else:
                st += " "
        answer.append(st)
    return answer