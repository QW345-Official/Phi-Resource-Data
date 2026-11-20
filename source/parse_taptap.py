import sys
import json
import re


def main():
    text = sys.stdin.read()

    # 从文本中找出所有以 {"data" 开头的行（允许前面有空白）
    candidates = re.findall(r'^\s*(\{"data".*?\})\s*$', text, flags=re.MULTILINE)
    if not candidates:
        # 兜底：找最后一个以 { 开头且含 "data" 的整行
        candidates = [
            line.strip()
            for line in text.splitlines()
            if line.strip().startswith("{") and '"data"' in line
        ]

    result = None
    for cand in candidates:
        try:
            obj = json.loads(cand)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and isinstance(obj.get("data"), dict) and "apk" in obj["data"]:
            result = obj

    if result is None:
        sys.exit("未找到含 data.apk 的合法 JSON")

    print(json.dumps(result))


if __name__ == "__main__":
    main()
