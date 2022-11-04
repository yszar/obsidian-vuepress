#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 1:14
# @Author  : yszar
# @FileName: main.py
# @Blog    : https://iamjy.com
# @Contact : yszaryszar@gmail.com
# @Version : 1.0.0
# !/usr/bin/env python"
# -*-coding:utf-8 -*-"
import argparse
import os
import re
from pathlib import Path


type_dict = {
    "info": "info",
    "abstract": "info",
    "example": "info",
    "note": "note",
    "quote": "note",
    "tip": "tip",
    "success": "tip",
    "warning": "warning",
    "question": "warning",
    "danger": "danger",
    "failure": "danger",
    "bug": "danger",
}


def get_version():
    return "0.0.1"


def parse_md(p):
    text = p.read_text()
    # 将匹配到的内容传入 convert 函数处理
    return re.subn(
        r"^>\s\[!([A-Za-z]+)].*?\s+$", convert, text, flags=re.S | re.M | re.I
    )


def convert(obj):
    # 仅有标题
    if re.search(r"^>\s\[!([A-Za-z]+)] .*?\s$", obj.group()) is not None:
        r = re.search(r"^>\s\[!([A-Za-z]+)]\s(.+)$", obj.group())
        type_name = type_dict[r.group(1)]
        title = r.group(2)
        return f"::: {type_name} {title}\n:::\n"
    # 仅有内容
    elif re.search(r"^>\s\[!([A-Za-z]+)]\n", obj.group()) is not None:
        r = re.search(r"^>\s\[!([A-Za-z]+)]\n", obj.group())
        type_name = type_dict[r.group(1)]
        body = re.findall(r"^> ([^[].*?)$", obj.group(), flags=re.M)
        body_str = "\n".join(body)
        return f"::: {type_name}\n{body_str}\n:::\n"
    # 有标题有内容
    elif re.search(r"^>\s\[!([A-Za-z]+)] .*\n", obj.group()) is not None:
        r = re.search(r"^>\s\[!([A-Za-z]+)]\s(.+)$", obj.group(), flags=re.M)
        type_name = type_dict[r.group(1)]
        title = r.group(2)
        body = re.findall(r"^> ([^[].*?)$", obj.group(), flags=re.M)
        body_str = "\n".join(body)
        return f"::: {type_name} {title}\n{body_str}\n:::\n"
    else:
        return None


def main():
    parser = argparse.ArgumentParser(description="用vuepress构建obsidian笔记时，转换提示块")
    # type是要传入的参数的数据类型  help是该参数的提示信息
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=get_version(),
        help="Display version",
    )
    parser.add_argument("-p", type=str, default="src", help="笔记所在目录")
    parser.parse_args()

    args = parser.parse_args()

    directory = args.p  # 文件夹名称
    # 遍历 args.p 下的所有文件，找出 markdown 文件
    print("========== 开始处理文件 ==========")
    file_count = 0
    text_count = 0
    for root, dirs, files in os.walk(directory):
        for f in files:
            p = Path(root + "/" + f)
            if p.suffix == ".md":
                # 将找出的 markdown 传入解析函数
                new_text = parse_md(p)
                p.write_text(new_text[0], encoding="utf-8")
                if new_text[1] != 0:
                    file_count += 1
                    text_count += new_text[1]
                    print("=====", p, "=====")
                    print(f"替换完成, 共替换{new_text[1]}处\n")

    print("========== 文件处理完成 ==========")
    print(f"本次共处理 {file_count} 个文件， {text_count} 处文本。")


if __name__ == "__main__":
    main()
