"""
Copy template in folder qnnn to new question folder based on input number
"""
import re
import shutil

q = input('Question number:')
qn = re.search(r"\d+", q)
shutil.copytree('qnnn', 'q'+qn.group(0))
