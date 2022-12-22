import os
import subprocess

def get_version():
    return os.getenv("VERSIONEER_OVERRIDE", default="8.0.beta")

def get_rev():
    return os.getenv("VERSIONEER_REV", default=subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip())
