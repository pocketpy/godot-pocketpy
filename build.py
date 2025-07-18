import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='Debug')
parser.add_argument('--platform', type=str, default='win32')

def run(cmd: str):
    print(cmd)
    code = os.system(cmd)
    assert code == 0

args = parser.parse_args()
config: str = args.config
platform: str = args.platform

extra_flags = []

if platform == 'android':
    extra_flags.append('-DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake')
    extra_flags.append('-DANDROID_PLATFORM=android-22')
    extra_flags.append('-DANDROID_ABI=arm64-v8a')
elif platform == 'ios':
    extra_flags.append('-DCMAKE_TOOLCHAIN_FILE=pocketpy/3rd/ios.toolchain.cmake')
    extra_flags.append('-DDEPLOYMENT_TARGET=13.0')
    extra_flags.append('-DPLATFORM=OS64')
else:
    run(f"cmake -B build -DCMAKE_BUILD_TYPE={config}")

run(f"cmake --build build --config {config}")
