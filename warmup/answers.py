"""
python_warmup.py 정답 예시 — 다 풀고 나서 비교용으로만 보세요!
정답은 하나가 아니에요. 테스트를 통과했다면 내 풀이도 정답입니다.

실행하면 이 정답들로 채점기를 돌려 봅니다:  py warmup/answers.py
"""

from collections import deque, Counter, defaultdict
import heapq


def p01_even_squares(nums):
    return [x * x for x in nums if x % 2 == 0]


def p02_make_grid(n, m):
    return [[0] * m for _ in range(n)]


def p03_sort_students(students):
    return sorted(students, key=lambda x: (-x[1], x[0]))


def p04_reverse_words(s):
    return " ".join(s.split()[::-1])


def p05_caesar(s, k):
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord("a") + k) % 26 + ord("a")))
        else:
            out.append(ch)
    return "".join(out)


def p06_most_common_char(s):
    cnt = Counter(s)
    return min(cnt, key=lambda ch: (-cnt[ch], ch))


def p07_group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return groups


def p08_two_sum_exists(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False


def p09_valid_brackets(s):
    pair = {")": "(", "]": "[", "}": "{"}
    st = []
    for ch in s:
        if ch in "([{":
            st.append(ch)
        elif not st or st.pop() != pair[ch]:
            return False
    return not st


def p10_k_smallest(nums, k):
    h = list(nums)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(k)]


def p11_josephus(n, k):
    q = deque(range(1, n + 1))
    order = []
    while q:
        q.rotate(-(k - 1))      # k-1명을 뒤로 보내고
        order.append(q.popleft())  # k번째 제거
    return order


def p12_shortest_path(grid):
    n, m = len(grid), len(grid[0])
    if grid[0][0] == 0:
        return -1
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist[n - 1][m - 1]


if __name__ == "__main__":
    import os
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from python_warmup import run
    run(globals())
