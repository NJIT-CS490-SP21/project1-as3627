import os
import random
from flask import Flask, render_template
from spoti import get_info

# These are temp: but belong to Arianna Grande, Lyn (Persona 5 OST), and Hollywood Principle 
ids = ['66CXWjxzNUsdJxJ2JdwvnR', '5qEtLvXzYdv0G7c7rR6irX', '6ldZGvFDjs6KafLouTBHJ9']

idx = random.randint(0, len(ids) - 1)

# Pass the random index through to get info for a randomly chosen artist. 
info = get_info(ids[idx])

for i in info:
    print(i)