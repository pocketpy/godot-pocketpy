import os
import sys

def run(cmd: str):
    print(cmd)
    code = os.system(cmd)
    assert code == 0

if len(sys.argv) > 1:
    config = sys.argv[1]
else:
    config = 'Debug'

run(f"cmake -B build -DCMAKE_BUILD_TYPE={config}")
run(f"cmake --build build --config {config}")