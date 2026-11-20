import sys
import ast
import json


def main():
    text = sys.stdin.read()

    result = None
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = ast.literal_eval(line)
        except (ValueError, SyntaxError):
            continue
        if (
            isinstance(obj, dict)
            and isinstance(obj.get("data"), dict)
            and "apk" in obj["data"]
            and isinstance(obj["data"]["apk"], dict)
            and "download" in obj["data"]["apk"]
        ):
            result = obj

    if result is None:
        sys.exit("未找到含 data.apk.download 的字典")

    print(json.dumps(result))


if __name__ == "__main__":
    main()
