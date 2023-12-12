#!/usr/bin/env python
# 참고: https://velog.io/@betterfuture4/%EA%B9%83%ED%97%88%EB%B8%8C-%EC%9E%94%EB%94%94%EC%97%90-%EB%AC%BC-%EC%A3%BC%EA%B8%B0feat.BaekjoonHub%EB%A1%9C-%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C-%EC%9E%90%EB%8F%99-%EC%97%85%EB%A1%9C%EB%93%9C

import os
from urllib import parse

HEADER="""# 
# 백준 & 프로그래머스 & LeetCode 문제 풀이 목록

"""

def main():
    content = ""
    content += HEADER
    
    directories = [];
    solveds = [];

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory not in directories:
            if directory in ["백준", "프로그래머스", "LeetCode"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 풀이 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        for file in files:
            if category not in solveds:
                content += "|{}|[풀이 보기]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                solveds.append(category)
                print("category : " + category)

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
