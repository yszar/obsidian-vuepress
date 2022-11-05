# obsidian-vuepress

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

obsidian-vuepress

使用 VuePress + obsidian 时，构建过程中使用脚本将一些 vuepress 不能识别不能渲染的格式转换成可以识别的格式。

## 内容列表
<!-- TOC -->
* [obsidian-vuepress](#obsidian-vuepress)
  * [内容列表](#)
  * [背景](#)
  * [安装](#)
  * [使用说明](#)
  * [维护者](#)
  * [如何贡献](#)
    * [贡献者](#)
  * [使用许可](#)
<!-- TOC -->

## 背景

因为用`obsidian`写笔记，同时也同步到`vuepress`上面，但是有些 markdown 格式并不通用，vuepress 不认识，不渲染，所以就有了这个项目，在 Github actions 中，vuepress 构建之前，将不渲染的那些格式转换为可以渲染的格式。

## 安装

目前还没打包，直接复制到 vuepress 项目根目录。

## 使用说明

### 使用前提条件
- vuepress 博客
  - vuepress-theme-hope 主题
- obsidian
  - admonition 插件

### 转换规则

| admonition 提示块 | 转为 vuepress-theme-hope 提示块 |
|----------------|----------------------------|
| info           | info                       |
| abstract       | info                       |
| example        | info                       |
| note           | note                       |
| quote          | note                       |
| tip            | tip                        |
| success        | tip                        |
| warning        | warning                    |
| question       | warning                    |
 | danger         | danger                     |
| failure        | danger                     |
| bug            | danger                     |


目前只支持`admonition`插件的以下三种格式

- 仅有标题

![](https://static.iamjy.com/blog-images/20221105164531.png-webp)

```
> [!success] obsidian-vuepress
> 
```

- 仅有内容，无标题

![](https://static.iamjy.com/blog-images/20221105164657.png-webp)

```
> [!success]
> I'm obsidian-vuepress
```

- 有标题有内容

![](https://static.iamjy.com/blog-images/20221105164741.png-webp)

```
> [!success] obsidian-vuepress
> I'm obsidian-vuepress
```

### 使用
```bash
python obsidian-vuepress.py src
# src 是我存放 markdown 源文件的目录
```

## 维护者

[@yszar](https://github.com/yszar)。

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/yszar/obsidian-vuepress/issues/new) 或者提交一个 Pull Request。

遵循 [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) 行为规范。

### 贡献者

感谢以下参与项目的人：

## 使用许可

[MIT](LICENSE) © yszar
