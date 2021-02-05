import os

from flask import Flask, render_template
from spoti import get_info


info = get_info('5qEtLvXzYdv0G7c7rR6irX')

for i in info:
    print(i)