#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
"""
__author__ = 'shede333'
"""

from .swtermcolor import SWTermColor

success = SWTermColor(prefix_text="✔:").c_blue()  # 特效
error = SWTermColor(prefix_text="✘:").c_red().a_bold()  # 特效
Warning = SWTermColor(prefix_text="❗️:").c_yellow()  # 特效
