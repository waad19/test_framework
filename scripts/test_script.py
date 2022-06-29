#!/usr/bin/env python3
import json
import os
import subprocess

TEST_VALUE = os.environ.get('TEST_VALUE').strip()
RESULTS_DIR = '/opt/project/results'


def print_json():
    """
    Produce JSON
    """
    filename = f'test_file_{TEST_VALUE}.json'
    cmd = subprocess.run(["docker", "images"], stdout=subprocess.PIPE, text=True)
    images_list = cmd.stdout
    with open(os.path.join(RESULTS_DIR, filename), 'w', newline='') as f:
        json.dump({'TEST_VALUE': TEST_VALUE, 'images': images_list}, f, indent=4)


if __name__ == '__main__':
    print_json()
