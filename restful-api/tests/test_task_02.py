import sys
import os

# Add the parent folder (restful-api) to Python's module search path
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))

from task_02_requests import fetch_and_print_posts

import pytest
from task_02_requests import fetch_and_print_posts

def test_of_def():
    fetch_and_print_posts()