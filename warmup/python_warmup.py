"""
Python 코테 문법 재활 드릴 (12문제)

사용법
  1. 각 함수의 `raise NotImplementedError` 를 지우고 직접 구현하세요.
  2. 터미널에서 실행:   py warmup/python_warmup.py
     (이 PC는 `python` 명령이 PATH에 없어서 `py` 런처를 써야 해요)
  3. 통과(✅) / 실패(❌) / 미구현(⬜) 이 표시됩니다.

규칙: 막히면 notes/python-코테-문법.md 를 봐도 OK.
      다 풀고 나면, 하루 뒤에 안 보고 다시 풀어보세요.
      정답 예시는 warmup/answers.py 에 있어요 (다 풀고 비교용).
"""

from collections import deque, Counter, defaultdict
import heapq


# ─────────────────────────── 1. 리스트 기초 ───────────────────────────

def p01_even_squares(nums):
    """짝수만 골라 제곱한 리스트를 반환. (리스트 컴프리헨션 한 줄로 도전)
    [1, 2, 3, 4] -> [4, 16]
    """
    raise NotImplementedError


def p02_make_grid(n, m):
    """n행 m열, 0으로 채운 2차원 리스트를 반환.
    ⚠️ grid[0][0] = 1 로 바꿨을 때 다른 행이 같이 바뀌면 안 됩니다.
    """
    raise NotImplementedError


# ─────────────────────────── 2. 정렬 ───────────────────────────

def p03_sort_students(students):
    """(이름, 점수) 리스트를 점수 내림차순, 점수가 같으면 이름 오름차순으로 정렬해 반환.
    [("kim", 90), ("lee", 95), ("ahn", 90)] -> [("lee", 95), ("ahn", 90), ("kim", 90)]
    """
    raise NotImplementedError


# ─────────────────────────── 3. 문자열 ───────────────────────────

def p04_reverse_words(s):
    """단어 순서를 뒤집은 문자열을 반환. (단어 사이 공백은 하나로)
    "I love python" -> "python love I"
    """
    raise NotImplementedError


def p05_caesar(s, k):
    """소문자 알파벳만 k칸 뒤로 밀기 (z 다음은 a). 나머지 문자는 그대로.
    ("abz!", 1) -> "bca!"
    힌트: ord, chr, % 26
    """
    raise NotImplementedError


# ─────────────────────────── 4. dict / Counter ───────────────────────────

def p06_most_common_char(s):
    """가장 많이 나온 문자를 반환. 개수가 같으면 알파벳순으로 앞선 것.
    "banana" -> "a",  "abab" -> "a"
    """
    raise NotImplementedError


def p07_group_by_length(words):
    """단어를 길이별로 묶은 dict 반환 (입력 순서 유지).
    ["hi", "abc", "yo", "a"] -> {2: ["hi", "yo"], 3: ["abc"], 1: ["a"]}
    힌트: defaultdict(list)
    """
    raise NotImplementedError


def p08_two_sum_exists(nums, target):
    """서로 다른 두 원소의 합이 target이 되는 쌍이 있으면 True. O(N)으로!
    ([2, 7, 11], 9) -> True,  ([3], 6) -> False,  ([3, 3], 6) -> True
    힌트: 지금까지 본 값을 set에 저장
    """
    raise NotImplementedError


# ─────────────────────────── 5. 스택 / 큐 / 힙 ───────────────────────────

def p09_valid_brackets(s):
    """괄호 ()[]{} 가 올바르게 짝지어졌으면 True.
    "([]{})" -> True,  "(]" -> False,  "((" -> False
    """
    raise NotImplementedError


def p10_k_smallest(nums, k):
    """가장 작은 k개를 오름차순 리스트로 반환. heapq를 써보세요.
    ([5, 1, 4, 2, 3], 3) -> [1, 2, 3]
    """
    raise NotImplementedError


def p11_josephus(n, k):
    """1~n번 사람이 원형으로 앉아 있고, k번째 사람을 계속 제거할 때 제거 순서를 반환.
    (7, 3) -> [3, 6, 2, 7, 5, 1, 4]
    힌트: deque.rotate 또는 popleft/append
    """
    raise NotImplementedError


# ─────────────────────────── 6. BFS ───────────────────────────

def p12_shortest_path(grid):
    """1은 길, 0은 벽. (0,0)에서 오른쪽 아래 끝까지 최단 칸 수(시작·끝 포함)를 반환.
    도달할 수 없으면 -1. 상하좌우로만 이동.
    [[1,1,0],
     [0,1,0],
     [0,1,1]] -> 5
    """
    raise NotImplementedError


# ═══════════════════════════ 채점기 (수정하지 마세요) ═══════════════════════════

def _check_grid(f):
    g = f(3, 2)
    if not (len(g) == 3 and all(row == [0, 0] for row in g)):
        return False
    g[0][0] = 1
    return g[1][0] == 0 and g[2][0] == 0


TESTS = [
    ("p01_even_squares", lambda f: f([1, 2, 3, 4]) == [4, 16] and f([]) == [] and f([-2, 5]) == [4]),
    ("p02_make_grid", _check_grid),
    ("p03_sort_students", lambda f: f([("kim", 90), ("lee", 95), ("ahn", 90)]) == [("lee", 95), ("ahn", 90), ("kim", 90)]),
    ("p04_reverse_words", lambda f: f("I love python") == "python love I" and f("  a   b ") == "b a" and f("solo") == "solo"),
    ("p05_caesar", lambda f: f("abz!", 1) == "bca!" and f("hello", 26) == "hello" and f("xyz", 3) == "abc"),
    ("p06_most_common_char", lambda f: f("banana") == "a" and f("abab") == "a" and f("zzy") == "z"),
    ("p07_group_by_length", lambda f: dict(f(["hi", "abc", "yo", "a"])) == {2: ["hi", "yo"], 3: ["abc"], 1: ["a"]}),
    ("p08_two_sum_exists", lambda f: f([2, 7, 11], 9) is True and f([3], 6) is False and f([3, 3], 6) is True and f([1, 2], 10) is False),
    ("p09_valid_brackets", lambda f: f("([]{})") is True and f("(]") is False and f("((") is False and f("") is True and f(")(") is False),
    ("p10_k_smallest", lambda f: f([5, 1, 4, 2, 3], 3) == [1, 2, 3] and f([7, 7, 1], 2) == [1, 7]),
    ("p11_josephus", lambda f: f(7, 3) == [3, 6, 2, 7, 5, 1, 4] and f(1, 1) == [1] and f(4, 1) == [1, 2, 3, 4]),
    ("p12_shortest_path", lambda f: f([[1, 1, 0], [0, 1, 0], [0, 1, 1]]) == 5
                                    and f([[1, 0], [0, 1]]) == -1 and f([[1]]) == 1),
]


def run(module_globals):
    passed = 0
    for name, check in TESTS:
        f = module_globals[name]
        try:
            ok = check(f)
            mark = "✅" if ok else "❌"
            passed += bool(ok)
        except NotImplementedError:
            mark = "⬜"
        except Exception as e:  # 구현 중 에러도 보여주기
            mark = f"❌ ({type(e).__name__}: {e})"
        print(f"{mark}  {name}")
    print(f"\n{passed}/{len(TESTS)} 통과")


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    run(globals())
