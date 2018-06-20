# datas
爬取某些网站数据，并且做可视化处理。

## 前提条件
使用该爬虫，需要满足以下条件：
* 安装python3环境，推荐3.5
* 安装Pycharm Community(可选)  

### Python安装
Windows:   
请到[Python3.5 Download Page](https://www.python.org/downloads/release/python-350/)下载，下载完成后，双击进行安装。全部选项默认即可。  
然后设置系统环境变量，将安装的Python路径加到`$PATH`环境变量即可，参看[Windows 设置 Python环境变量](https://jingyan.baidu.com/article/48206aeafdcf2a216ad6b316.html)。  

Linux(Ubuntu为例):
```bash
sudo apt install python3.5
```  

Mac OS:
```bash
brew install python3
```  

### Pycharm Community安装
进入[Pycharm Community Download](https://www.jetbrains.com/pycharm/)下载，默认安装即可。

## 使用
首先需要下载本仓库代码，有以下两种方式:
* 到项目主页下载ZIP压缩文件，推荐不熟悉Git的用户
* 使用Git克隆，命令如下

```bash
cd $YOUR_WORK_DIR
git clone https://github.com/luozhouyang/datas
```
下载后解压（如果是下载ZIP压缩文件），然后使用你喜欢的文本编辑器或者IDE打开项目即可。推荐Pycharm Community。

然后按照Pycharm的提示安装依赖库。  

该代码主要有以下几个步骤：
* 下载html页面(保存数据源，不是很必要)
* 解析html文件，提取有效信息，保存为CSV文件
* 进一步处理CSV文件，提取出想要的数据，输出到EXCEL表格
* 将感兴趣的内容，绘制图表

进一步，你可以使用EXCEL进一步将输出的数据进行可视化。

### HTML页面的下载
网站一般会有反爬虫策略，常用的办法是控制访问的频率，同时使用多个IP。为了简单，本项目没有使用IP池，只是控制了访问频率。  
下载HTML页面的代码位于[bajiuwang/html_downloader.py](bajiuwang/html_downloader.py)。
本爬虫目前只支持`url+$ID`形式的网站页面下载，当然要想支持其他类型的URL很简单。  
举个例子，如果某网站的地址规律是`http://www.555.com?id=$ID`这种形式，那么本项目适合你，只需要给在Downloader的__init__函数里面，给`base_url`参数设置为`http://www.55.com?id=`。  
为了避免不必要的网络访问，你需要确定一个合理的`$ID`范围。在Downloader的__init__函数的`ranges`参数设置好即可。  

准备好之后，即可运行`html_downloader.py`程序，下载程序启动后，会定期保存当前的`$ID`值，当程序异常退出的时候，下次启动程序，会从该`$ID`开始继续下载，即类似断点功能。
记录该`$ID`的文件在程序当前目录，名为的`record.txt`文件。  
下载的HTML页面默认保存在本项目的根目录下的文件夹，具体目录你可以自己设置。

### HTML页面的解析
下载好数据之后，即可启动解析程序，提取出你想要的信息。按照[bajiuwang/patterns.py](bajiuwang/patterns.py)的格式添加需要解析的内容。  
运行[bajiuwang/html_parser.py](bajiuwamg/html_parser.py)文件，即可开始解析。  
如果你设置了其他的下载目录，在改文件的`file`一行改成你自定义的目录即可。  
本步骤生成的CSV文件位于前一步骤的相同目录，文件名为`0_info.csv`，你可以在`html_parser.py`文件中自行更改文件名。  

### 根据CSV文件进行可视化  
根据前面步骤生成的CSV文件，可以进一步可视化。使用`matplotlib`和`PrettyTable`两个库进行图的绘制和表格的输出。  

要生成图表，只需要运行[bajiuwang/csv_visualizer.py](bajiuwang/csv_visualizer.py)文件即可。
生成的图片保存在当前目录的`images`文件夹内。输出的表，直接打印在终端。  

同时也会将数据输出到EXCEL表格文件，保存在当前目录下的`datas.xlsx`文件，方便用户处理。

### 使用EXCEL处理输出文件  
上一个步骤输出的`datas.xlsx`文件，使用强大的Microsoft Excel软件打开，可以用来制作各种类型的图表。

## matlibplot中文显示的问题  
参考 [matlibplot显示中文](https://monkey0105.github.io/2016/10/10/matplotlib-chinese-display/)  

## License
   Copyright 2018 luozhouyang.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.