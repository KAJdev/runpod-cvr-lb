import runpod
import subprocess


def handler(job):
    """get CUDA version"""

    output = subprocess.check_output(["nvcc", "--version"]).decode("utf-8")
    return output.split("\n")[3]


# asedfkmeaklwfm

runpod.serverless.start({"handler": handler})
