# Summary:

This repo stores the practice of Data Structure and Algorithm challenges on [leetcode.com](leetcode.com) using Python 3. This has a few highligted advantages over coding directly on [leetcode.com](leetcode.com)'s IDE:

- Testing is set up locally with pytest and VSCode testing framework and can run conveniently without hitting rate limiting or user' rating on [leetcode.com](leetcode.com)
  ![testing](https://github.com/tinutmap/leetcode.com/blob/master/static/testing.png?raw=true)
- Abstraction classes and methods for commonly used structures such as linked list, binary tree, n_rary tree etc. have already been coded and tested by the author. See details in and implementation in `./linked_list/base.py`, `./binary_tree/base.py`, `./n_rary_tree/base.py` and files that import those.

# Prerequisites:

- VSCode Editor (optional) if user desires to utilize the testing framework
- Git (optional) if user wants Version Control in place.
- Python 3.11 or higher

# Setup

- Install pipenv:

```
pip install --user pipenv
cd project_folder
pipenv shell
pipenv install
```

## Start new question:

- At project root run `python -m new_q`
