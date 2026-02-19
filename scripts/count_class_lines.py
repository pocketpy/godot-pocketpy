"""统计 classes.pyi 中每个 class 的行数，从多到少排序输出。"""

import re

FILE = r"g:\repos\godot-pocketpy\demo\addons\godot-pocketpy\typings\godot\classes.pyi"

with open(FILE, encoding="utf-8") as f:
    lines = f.readlines()

classes: list[tuple[str, int]] = []   # (class_name, line_count)
current_class: str | None = None
current_start: int = 0

for i, line in enumerate(lines):
    if re.match(r"^class \w+", line):
        # 保存上一个 class
        if current_class is not None:
            classes.append((current_class, i - current_start))
        current_class = line.split("(")[0].split(":")[0].replace("class ", "").strip()
        current_start = i

# 最后一个 class
if current_class is not None:
    classes.append((current_class, len(lines) - current_start))

classes.sort(key=lambda x: x[1], reverse=True)

total_classes = len(classes)
total_lines = sum(c[1] for c in classes)
print(f"共 {total_classes} 个 class，合计 {total_lines} 行\n")
print(f"{'排名':>4}  {'Class 名称':<45} {'行数':>6}")
print("-" * 60)
for rank, (name, count) in enumerate(classes, 1):
    print(f"{rank:>4}  {name:<45} {count:>6}")
