import runpod
import subprocess


def handler(job):
    """get CUDA version"""

    output = subprocess.check_output(["nvcc", "--version"]).decode("utf-8")
    smi = subprocess.check_output(["nvidia-smi"]).decode("utf-8")
    return output.split("\n")[4] + "\n" + smi


runpod.serverless.start({"handler": handler})
