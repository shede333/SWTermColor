# _*_ coding:UTF-8 _*_
"""
__author__ = 'shede333'
"""

from swtermcolor import SWTermColor

print(SWTermColor("hello, sw "))
print(SWTermColor("hello, sw red").c_red())
print(SWTermColor("hello, sw red").c_blue().c_red())
print(SWTermColor().text("hello, sw red replace").c_red())
print(SWTermColor("hello, sw red bg_grey").c_red().b_grey())
print(SWTermColor("hello, sw red bg_blue").c_red().b_blue())
print(SWTermColor("hello, sw red bg_blue").c_red().b_white().b_blue())  # 背景色，蓝色 覆盖了 白色
print(SWTermColor("hello, sw red bg_blue bold").c_red().b_blue().a_bold())
print(SWTermColor("hello, sw red bg_blue bold dark").c_red().b_blue().a_bold().a_dark())
print(SWTermColor("hello, sw red blue bold reverse(反转)").c_red().b_blue().a_bold().a_reverse())

text = "hello, sw red bg_blue bold 文本 与 样式 分离"
effect = SWTermColor().c_red().b_blue().a_bold()
print(effect)  # 输出空行
print(effect(text))  # 正常使用方法
print(effect(text, "color临时改为grey", color="grey"))  # 临时改变文本颜色
print(effect(text, "bg_color临时改为grey", bg_color="grey"))  # 临时改变文本背景色
print(effect(text, "attrs临时改为reverse", attrs=["reverse"]))  # 临时改变文本效果
print(effect.text("提示文案:"))  # 增加 提示文案
print(effect(text, sep=" *#sep#* "))  # 输出：提示文案 + text，以sep做分隔符
effect.text(None)  # 删除默认的提示文案
# 输出彩色的：1 + 2 = 3
print(effect(" 1") + effect(" + ", bg_color="cyan") + effect("2") + effect(" = ", bg_color="cyan") + effect("3 "))
