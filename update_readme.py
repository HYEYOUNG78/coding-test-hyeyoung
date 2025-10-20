import os
from datetime import date

# 문제 풀이가 들어있는 폴더만 지정
TARGET_DIRS = ["python", "java", "sql"]
README_PATH = "README.md"

def count_files_by_lang():
    counts = {"Python": 0, "Java": 0, "SQL": 0}
    for target in TARGET_DIRS:
        if not os.path.exists(target):
            continue
        for root, _, files in os.walk(target):
            for file in files:
                if file.endswith(".py"):
                    counts["Python"] += 1
                elif file.endswith(".java"):
                    counts["Java"] += 1
                elif file.endswith(".sql"):
                    counts["SQL"] += 1
    return counts

def update_readme():
    counts = count_files_by_lang()
    today = date.today().strftime("%Y-%m-%d")

    table = f"""
## 📊 코딩테스트 문제 통계 (자동 업데이트)

| 언어 | 문제 수 | 최근 업데이트 |
|------|----------|----------------|
| Python | {counts['Python']} | {today} |
| Java | {counts['Java']} | {today} |
| SQL | {counts['SQL']} | {today} |
"""

    if not os.path.exists(README_PATH):
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(table)
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if "## 📊 코딩테스트 문제 통계" in content:
        start = content.index("## 📊 코딩테스트 문제 통계")
        content = content[:start] + table
    else:
        content += "\n" + table

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
    print("✅ README 자동 업데이트 완료! 변경 내용을 확인하세요.")