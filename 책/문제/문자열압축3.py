def solution(s):
    min_value = 1e9
    for step in range(1, len(s)//2 +1):
        count = 1
        pre = s[0:step]
        compressed = ''
        for j in range(step, len(s), step):
            if pre == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + pre if count >= 2 else pre
                pre = s[j:j+step]
                count = 1
        compressed += str(count) + pre if count >= 2 else pre
        min_value = min(min_value,len(compressed))
        print(compressed)
    return min_value

print(solution("aabbaccc"))