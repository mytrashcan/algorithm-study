# Python 코테 문법 치트시트

코딩테스트에 자주 쓰이는 것만 모았어요. 위에서부터 순서대로 훑어보면 돼요.

---

## 1. 입출력

```python
import sys
input = sys.stdin.readline          # 백준: 입력이 많을 때 필수 (속도)

n = int(input())                    # 정수 하나
a, b = map(int, input().split())    # 정수 여러 개
arr = list(map(int, input().split()))           # 한 줄을 리스트로
grid = [list(map(int, input().split())) for _ in range(n)]  # 2차원
s = input().strip()                 # 문자열 (readline은 끝에 \n이 붙음 → strip)

print(*arr)                         # 1 2 3  (공백으로 구분해 출력)
print("\n".join(map(str, arr)))     # 한 줄에 하나씩, 빠르게 출력
```

> 프로그래머스는 `def solution(...)`의 인자로 입력이 들어오고 `return`으로 답을 내요. 입출력 코드가 필요 없어요.

---

## 2. 리스트

```python
a = [0] * n                         # 길이 n, 0으로 초기화
g = [[0] * m for _ in range(n)]     # n×m 2차원 (⚠️ [[0]*m]*n 은 같은 행을 공유해서 버그)

a.append(x); a.pop(); a.pop(0)      # pop(0)은 O(N) → 큐가 필요하면 deque
a[-1]                               # 마지막 원소
a[1:4], a[::-1]                     # 슬라이싱, 뒤집기
len(a), sum(a), max(a), min(a)
a.index(x), a.count(x)              # O(N)
x in a                              # O(N)  ← 반복문 안에서 쓰면 느림, set/dict 사용

[x * 2 for x in a if x > 0]         # 리스트 컴프리헨션
for i, x in enumerate(a): ...       # 인덱스와 값 같이
for x, y in zip(a, b): ...          # 두 리스트 같이 돌기
```

---

## 3. 정렬

```python
a.sort()                            # 제자리 정렬
b = sorted(a)                       # 새 리스트 반환
sorted(a, reverse=True)             # 내림차순
sorted(words, key=len)              # 길이순
sorted(pairs, key=lambda x: (x[1], -x[0]))  # 2번째 오름차순, 같으면 1번째 내림차순
```

---

## 4. 문자열

```python
s.split()        # 공백 기준 분리          s.split(",")  # 구분자 지정
" ".join(lst)    # 리스트 → 문자열 (원소가 str이어야 함)
s[::-1]          # 뒤집기
s.upper(), s.lower(), s.isdigit(), s.isalpha()
s.replace("a", "b"), s.count("a"), s.find("ab")   # find는 없으면 -1
s.startswith("ab"), s.endswith("z")
ord("a"), chr(97)                    # 문자 ↔ 숫자 (97 = 'a')
f"{name}: {score:.2f}"              # f-string 포매팅
```

> 문자열은 **수정 불가(immutable)**. 여러 번 이어 붙일 땐 리스트에 모았다가 `"".join()`.

---

## 5. dict / set (해시) — O(1) 조회

```python
d = {}
d[key] = d.get(key, 0) + 1          # 없으면 0에서 시작해 개수 세기
for k, v in d.items(): ...
key in d                            # O(1)

from collections import Counter, defaultdict
cnt = Counter(["a", "b", "a"])      # {'a': 2, 'b': 1}
cnt.most_common(1)                  # [('a', 2)]
Counter(a) - Counter(b)             # 개수 빼기 (0 이하는 사라짐)

g = defaultdict(list)               # 없는 키 접근 시 빈 리스트 자동 생성
g[u].append(v)                      # 그래프 인접 리스트에 편함

s = set(); s.add(x); s.discard(x)
a_set & b_set, a_set | b_set, a_set - b_set   # 교집합, 합집합, 차집합
```

---

## 6. 큐 / 스택 / 힙

```python
# 스택: 그냥 리스트
st = []; st.append(x); st.pop(); st[-1]

# 큐: deque (BFS 필수)
from collections import deque
q = deque([start])
q.append(x); q.popleft()            # 양쪽 끝 모두 O(1)

# 힙(우선순위 큐): 최소 힙
import heapq
h = []
heapq.heappush(h, 3)
heapq.heappop(h)                    # 가장 작은 값
heapq.heapify(lst)                  # 리스트를 힙으로 (O(N))
heapq.heappush(h, -x)               # 최대 힙은 부호를 뒤집어서
heapq.heappush(h, (dist, node))     # 튜플은 첫 원소 기준 정렬
```

---

## 7. 자주 쓰는 틀

### BFS (격자 최단거리)
```python
from collections import deque

def bfs(grid, sr, sc):
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist
```

### DFS (재귀)
```python
import sys
sys.setrecursionlimit(10**6)        # ⚠️ 재귀 DFS 쓸 땐 필수 (기본 한도 1000)

def dfs(v):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)
```

### 완전탐색 도구
```python
from itertools import permutations, combinations, product
list(permutations([1, 2, 3], 2))    # 순열 (순서 O)
list(combinations([1, 2, 3], 2))    # 조합 (순서 X)
list(product([0, 1], repeat=3))     # 중복 순열 (모든 경우)
```

### 이분 탐색
```python
from bisect import bisect_left, bisect_right
bisect_left(sorted_a, x)            # x 이상이 처음 나오는 위치
bisect_right(sorted_a, x) - bisect_left(sorted_a, x)   # 정렬된 리스트에서 x의 개수
```

---

## 8. 자주 하는 실수

| 실수 | 해결 |
|------|------|
| `[[0]*m]*n` 으로 2차원 생성 | `[[0]*m for _ in range(n)]` |
| 반복문 안에서 `x in list` | `set`이나 `dict`로 바꾸기 |
| `list.pop(0)` 로 큐 구현 | `deque.popleft()` |
| 재귀 DFS에서 RecursionError | `sys.setrecursionlimit(10**6)` 또는 BFS/스택으로 |
| 백준에서 `input()` 시간초과 | `sys.stdin.readline` |
| 큰 수 나눗셈 `/` 사용 | 정수 몫은 `//`, 나머지는 `%` |
| 무한대 초기값 | `float('inf')` 또는 `10**18` |

## 9. 시간 감각 (Python 기준, 대략 1초 ≈ 2,000만 번 연산)

| N 크기 | 가능한 복잡도 |
|--------|---------------|
| ~ 10 | O(N!) 순열 완전탐색 |
| ~ 20 | O(2^N) 부분집합 |
| ~ 500 | O(N³) |
| ~ 5,000 | O(N²) |
| ~ 100만 | O(N log N) 정렬, 힙 |
| 그 이상 | O(N), O(log N) |
