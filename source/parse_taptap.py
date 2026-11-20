import sys
import json


def main():
    result = None
    for line in sys.stdin:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if (
            isinstance(obj, dict)
            and isinstance(obj.get("data"), dict)
            and "apk" in obj["data"]
        ):
            result = obj

    if result is None:
        sys.exit("未找到含 data.apk 的合法 JSON")

    print(json.dumps(result))


if __name__ == "__main__":
    main()
