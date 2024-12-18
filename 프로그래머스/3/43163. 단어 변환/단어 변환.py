from collections import deque

def solution(begin, target, words):

    if target not in words: # 변환할 수 없는 경우 
        return 0 
    
    def bfs(begin, target, words):
        queue =deque()
        queue.append([begin, 0]) # (현재 단어, 변환 횟수)

        while queue:
            now, step = queue.popleft()

            if now == target:
                return step 

            for word in words:
                count = 0 # 다른 글자수 카운트 
                for i in range(len(now)):
                    if now[i] != word[i]:
                        count += 1 

                if count == 1: # 한 글자만 다르면 변환 가능 
                    queue.append([word, step+1]) # 큐에 추가 (다음 단어, 변환 횟수+1)

    return bfs(begin, target, words)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
