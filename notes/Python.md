## 1.注释：  
+ 以 '#'开头，为单行注释；以'''comment'''为多行注释  
## 2.命名与保留字：
+ 规则：数字、字母、下划线和汉字，区分大小写，首字母非数字，不能为保留字  
## 3.数据类型：
+ 字符串类型:""或''均可，分为*正向递增序号*与*反向递减序号*；
  - 索引：`<字符串>[M]`，返回字符串中的单个字符  
  - 切片：`<字符串>[M:N]`，返回字符串中的一段字符串  
+ 数字类型：整数、浮点数
+ 列表类型：[]，采用逗号分隔各元素，['F','f']  
+ eval():去除参数最外侧引号并执行余下语句，eval("1+2") 
## 4.Turtle库，也是(海龟)啦：
### 4.1 绘图窗体：从左上角(0,0)开始:  
    # 设置窗体大小及位置，后两个参数可选
    turtle.setup(width, height, starx, starty)  
### 4.2 绝对坐标：
	# 开始海龟在画布中心(0,0)，X轴由右左向，Y轴由下到上
    turtle.goto()
### 4.3 海龟坐标：
	turtle.circle(r,angel)
	turtel.fd(d)	# 前进
	turtle.bk(d)	# 后退
### 4.4 turtle角度坐标系：
	逆正顺负，以前进为标准，逆时针：前-左-后-右，即前的逆时针左，顺时针为右
	turtle.seth(angle)	# 改变海龟行进角度
	turtle.left(angle) 	# 朝左改变角度
	turtle.right(angle)	# 朝右改变角度
### 4.5 turtle RGB 色彩模式：
+ ### 0~255整数值或者0~1小数值
        White-255,255,255	yellow-255,255,0
    	magenta-255,0,255	cyan-0,255,255
    	blue-0,0,255		black-0,0,0
		turtle.colormode(mode)	# 

## 5.Turtle语法元素分析：
### 5.1 turtle 画笔控制函数：
	turtle.penup()	# 抬起画笔，海龟在飞行，turtle.pu()
	turtle.pendown() # 落下画笔，海龟在爬行，turtle.pd()
	turtle.pensize(width) # 画笔宽度，海龟的腰围，turtle.width(width)
	turtle.pencolor(color) # 画笔颜色，color-字符串或者RGB
### 5.2 turtl运动控制函数：
	turtle.forward(d)	# 走直线，turtle.fd(d)
	turtle.circle(r, extent=none) # 走曲线，r绘制半径，默认圆心在海龟左侧r距离的位置，决定海龟运动方向，extent绘制角度，默认是360°	
### 5.3 turtle 方向控制函数(绝对角度+海龟角度)：
	turtle.setheading(angle)	# 改变海龟行进角度，turtle.seth(angle)
	turtle.left(angle) 	# 朝左改变角度
	turtle.right(angle)	# 朝右改变角度
## 6. 库引用：
### 6.1使用方法：

    import <库名>
	<库名>.<函数名>(<函数参数>)	
	
	from <库名> import <函数名>  	
	from <库名> import* 
	<函数名>(<函数参数>)
	
	import <库名> as <库别名>
	<库别名>.<函数名>(<函数参数>)

## 7. 程序控制结构：
### 7.1 for循环：
	for <变量> in range (<参数>)：			for <循环变量> in <遍历结构>
		<循环执行的语句>							<语句块>
	range(N)：产生0~(N-1)整数序列，共N个
	range(M,N)：产生M~(N-M)整数序列，共N-M个
### 7.2 分支结构：
	if <条件>：			if<条件>				if<条件1>	
		<语句块>  			<语句块1>			<语句块1>
						else:				elif:<条件2>
							<语句块2>			<语句块2>
											else:
												<语句块3>
	<语句块1> if <条件> else <语句块2>
	
### 7.3 条件组合：
+ x and y --> 逻辑与
+ x or y --> 逻辑或
+ not x --> 逻辑非
### 7.4 异常处理：
	try:				try:					try:
		<语句块1>			<语句块1>				<语句块1>
	except:				except<异常类型>:		except:
		<语句块2>			<语句块2>				<语句块2>
												else:
													<语句块3>
												finally:
													<语句块4>
### 7.5 无限循环：
	while <条件>：
		<语句块>
+ break:跳出并结束当前整个循环，执行循环后的语句
+ continue:结束当次循环，据需执行后续次数循环
## 8.基本数据类型：
### 8.1整数：
+ 十进制：1010，99，-127
+ 二进制：0b010，-0B101
+ 八进制：0o123，-0O456	
+ 十六进制：0x9a，-0X89
### 8.2浮点数：
+ 浮点数运算存在不确定尾数
	round(x,d)：对x四舍五入，d为小数截取位数
+ 使用字母e/E作为幂的符号，以10为基数，4.3e-3，9.6E5 
### 8.3 复数
+ z = 1.23e-4+5.6e+89j # z.real z.imag
### 8.4 数字类型及操作：
+ `x+y、x-y、x*y、x/y、x//y(10//3=3)`
+ `+x x自身；-y y的负值；x%y 取余；x**y 幂运算`
+ `x+=y、x-=y、x*=y、x/=y、x//=y、x%=y、x**=y`
+ 整数 ->浮点数 ->复数  
### 8.4 字符串：
+ 由一对单引号或双引号表示
  - "北京欢迎您！" 或者'C'
+ 字符串是字符的有序序列，可以对其中的字符进行索引
  - "北"是"北京欢迎您！"的第0个字符
+ 由一对三单引号或三双引号表示多行字符串
  - '''这里既有单引号(')又有双引号(")'''
+ 索引：`<字符串>[M]`，返回字符串中的单个字符  
+ 切片：`<字符串>[M:N]`，返回字符串中的一段字符串 
  - `<字符串>[M:N:K]` 根据步长K，切片
+ 转义符 \
  - 转义符表达特定字符的本意 \n \r
+ 操作符：
  - `x+y 连接两个字符串x和y`
  - `n*x 或 x*n n为整数，复制n次字符串x`
  - `x in s 如果x是s的子串，返回True，否则返回False`
+ 字符串处理函数：
  - `len(x) -- 返回字符串x的长度`
  - `str(x) -- 任意类型x所对应的字符串形式  eval()`
  - `hex(x)或oct(x) -- 整数x的十六进制或八进制小写形式字符串`
  - `chr(u) -- u为Unicode编码，返回其对应的字符`
  - `ord(x) -- x为字符，返回其对应的Unicode编码`
+ 字符串处理方法：
  - `str.lower()或str.upper()` -- 返回字符串副本，全部字符小写/大写
     eg:"appple.lower()"

  - `str.split(sep=None)` -- 返回一个**列表**，由str根据sep被分隔得部分组成，默认采用空格
     eg:"1,2,3,4,5".split(",")

  - `str.count(sub)` -- 返回子串sub在str中出现的次数  
     eg:"Apple".count("p")

  - `str.replace(old, new)` -- 返回字符串副本，所有old子串被替换为new  
	 eg:"Xingyue".replace("Xing", "An")

  - `str.center(width[,fillchar])` -- 字符串str根据width居中，fillchar可选  
	 eg:"AnXiaoHong".center(20, "+")

  - `str.strip(chars)` -- 从str中去掉在其左侧和右侧chars中列出的字符  
     eg:"python".strip(" =np")

  - `str.join(iter)` -- 在iter变量除最后一个元素外每个元素后增加一个str   
     eg: ",".join("12345")	
+ 字符串类型的格式化：
  - 字符串格式化使用.format()方法，<模版字符串>.format(<逗号分隔得参数>)
  eg:`"{}:计算机{}的CPU占用率为{}%".format("2019-04-21","C",10)`

+ {<参数序号>:<格式控制标记>}
  - <填充> <对齐> <宽度>
  eg:`"{0:=^20}".format("PYTHON")`	# < 左对齐，> 右对齐，^ 居中对齐
  - <,> <.精度> <类型>
  eg:`"{0:,.2f}.format(12345.6789)"`
  
## 9. time库的使用 import time
### 9.1 获取时间函数
+ time() -- 获取当前时间戳，计算机内部时间值，浮点数
+ ctime() -- 获取当前时间并以易读方式表示，返回字符串
+ gmtime() -- 获取当前时间，表示为计算机可处理的时间格式
### 9.2 时间格式化函数
+ strftime(tpl, ts) -- tpl是格式化模版字符串，ts是计算机内部时间类型变量
  - eg:`time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())`
+ strptime(str, tpl) -- str是字符串形式的时间值，tpl是格式化模版字符串，用来定义输入效果
  - eg:`time.strptime('2018-01-26 12:55:20', "%Y-%m-%d %H:%M:%S")`
### 9.3 程序计时
+ perf_counter() -- 返回CPU级别的时间计数值，由于计数起点不确定，连续调用差值有意义
+ sleep() -- s拟休眠时间，秒/浮点数均可
## 10. random库
+ seed(a=None) -- 初始化给定的随机数种子，默认当前系统时间
+ random() -- 生成一个[0.0,1.0]之间的随即小数

+ randint(a,b) -- 生成一个[a,b]之间的整数
+ randrange(m,n[,k]) -- 生成一个[m,n]之间以k步长的随即整数
+ getrandbits(k) -- 生成k比特长的随机数
+ uniform(a,b) -- 生成一个[a,b]之间的随即小数
+ choice(seq) -- 从序列seq中随即选取一个元素
+ shuffle(seq) -- 将序列seq中元素随即排列，返回打乱后的序列
###  11.函数
#### 11.1 函数的定义：
	def <函数名> (<参数(0个或多个)>):	  def fac(n):				def fac(n):
		<函数体>							 s = 1						if(n==0):
		return <返回值>					 for i in range(1,n+1):			return 1
											s *= i					else:
										 return s						return n*fac(n-1)
#### 11.2 局部变量和全局变量：
+ 局部变量和全局变量是不同的变量，函数运行结束后，局部变量被释放
+ global关键字在函数内部声明此变量为全局变量
+ 局部变量为组合数据类型且未创建，等同于全局变量
+ lambda函数
  - lambda函数是一种匿名函数，返回函数名作为结果
  - <函数名> = lambda <参数> :<表达式>
  - `f = lambda x, y : x + y`

### 12. PyInstall库：
+ .py --> PyInstall --> .exe `pip install pyinstall`
+ 使用：
  - `pyinstaller -F <文件名.py>` 打包生成.exe
  - `pyinstaller -h` 查看帮助
  - `pyinstaller --clean`	清理临时文件
  - `pyinstaller -i <图标文件名.ico>`

### 13. 组合数据类型
+ **集合**类型：
  - 集合用大括号{}表示，元素用逗号分隔，建立集合用{}或者set{}，元素唯一，无顺序之分
     * eg:`A = {"python", "JAVA",("C","C++")}`
     * eg:`B = set("PYPY123")`
+ **集合**运算：
  - `S|T：返回一个新集合，包括在集合S和T中的所有元素`  并操作
  - `S-T：返回一个新集合，包括在集合S但不包括T中的元素` 减操作
  - `S&T：返回一个新集合，包括同时在S与T中的元素` 	交操作
  - `S^T：返回一个新集合，包括集合S与T中非相同元素` 补操作
+ **集合**处理方法：
  - `S.add(x) -- 如果x不在集合S中，增加x`
  - `S.discard(x) -- 移除S中元素x，如果x不在集合S中，不报错`
  - `S.remove(x) -- 移除S中元素x，如果x不在集合S中，KeyError异常`
  - `S.clear() -- 移除S所有元素`
  - `S.pop() -- 随即返回一个元素，更新S，S若为空，产生KeyError异常`
  - `S.copy() -- 返回集合S的一个副本`
  - `len(S) -- 返回集合S元素个数`
  - `x in S -- 判断S中元素x是否存在`
  - `x not in S -- 判断S中元素x是否不存在`
+ 序列类型
  - 字符串类型、列表类型、元组类型
  - 操作符：`x in s，x not in s，s + t，s*n 或 n*s，s[i]，s[i:j]，s[i:j:k]`
  - 方法：`len(s)，min(s)，max(s)，s.index(x)、s.index(x,i,j)，s.count(x)`
  - **元组**是一种序列类型，一旦被创建就不能被修改，使用()或者tuple()创建，用逗号分隔，()不是必须的
  - **列表**是一种序列类型，可以修改，使用[]或者list()创建，用逗号分隔
     * `ls[i] = x，ls[i:j:k] = lt，del ls[i]，del ls[i:j:k]，ls += lt，ls*=n`
     * `ls.append(x)，ls.clear()，ls.copy()，ls.insert(i,x)，ls.pop(i)，ls.remove(x)，ls.reverse()`
  - **字典**类型 (映射:键(索引)和值(数据)的对应)，使用{}或者dict{}创建，键值对用冒号表示
  - 字典操作：  
     * `d["a"] = 1 -- d中新增键值对`   
     * `del d[k] -- 删除字典d中键k对应的数据`
     * `k in d -- 判断键k是否存在字典d中`
     * `d.keys() -- 返回字典d中所有键的信息`
     * `d.values() -- 返回字典d中所有值的信息`
     * `d.get(k,<default>) -- 键k存在，返回对应值，不存在返回<default>值`
     * `d.pop(k,<default>) -- 键k存在，取出对应值，不存在返回<default>值`
     * `d.popitem() -- 随即从字典中取出一个键值对，以元组形式返回`
     * `d.clear() -- 删除所有键值对`
     * `len(d) -- 返回键值对个数`
     * `list(d.items()) -- 字典类型转为列表类型`
### 14.jieba库：
+ jieba是优秀的中文分词第三方库，`pip install jieba`
+ 三种模式：精确模式、全模式、搜索引擎模式
  * jieba.lcut(s) -- 精确模式，返回一个列表类型的分词结果
  * jieba.lcut(s,cut_all=True) -- 全模式，存在冗余
  * jieba.lcut_for_search(s) -- 存在冗余
  * jieba.add_word(w) -- 向分词词典中增加新词w
### 15. 文件：
#### 15.1 文件的打开 -- 操作 -- 关闭
+ file = open(<文件名>,<打开模式>)
  * 文件的打开： 
     + "D:/PYE/f.txt"
     + 'r' -- 只读模式，默认值，文件不存在，返回FileNotFoundError
     + 'w' -- 覆盖写模式，文件不存在创建文件
     + 'x' -- 创建写模式，文件不存在创建，存在返回FileExistsError
     + 'a' -- 追加写模式，文件不存在创建，存在在文件最后追加内容
     + 'b' -- 以二进制模式打开文件	't' -- 以文本模式打开文件
     + '+' -- 与r/w/x/a一同使用，在原功能上增加读写功能
  * 文件的操作：
     + <f>.read(size=-1) -- 读入全部内容，参数读入前size长度
     + <f>.readline(size=-1) -- 读入一行内容，参数读入该行的size长度
     + <f>.readlines(hint=-1) -- 读入所有行内容，以每行为元素形成列表，参数读入前hint行
	 + <f>.write(s) -- 向文件写入一个字符串或字节流
     + <f>.writelines(lines) -- 将元素全为字符串的列表写入文件
	 + <f>.seek(offset) -- 改变当前文件操作指针的位置，offset:0-文件开头，1-当前位置，2-文件结尾


#### 15.2 文件全文本操作：
    fname = input("输入文件名称:")	fname = input("输入文本名称")
	fo = open(fname, "r")			fo = open(fname,"r")
    txt = fo.read() 				txt = fo.read(2)
    处理文件							while txt != "":
    fo.close							处理文件
										txt = fo.read(2)
									fo.close()
	
	fname = input("输入文件名称:")	fname = input("输入文本名称")
	fo = open(fname, "r")			fo = open(fname,"r")
    for line in fo.readlines(): 	for line in fo:
    	print(line)						print(line)
    fo.close 						fo.close()	
### 16.wordcloud库：
#### 16.1 使用说明：
+ 实例化对象：w = worldcloud.WordCloud() 
  - `w.generate(txt) -- 向WorldCloud对象w中加载文本txt`
  - `w.to_file(filename) -- 将词云输出为图像文件`
+ 1、配置对象参数 2、加载词云文本 3、输出词云文件
+ w = worldcloud.WordCloud(<参数>)
  - `width -- 图片宽度，默认400px width=400px`
  - `height -- 图片高度，默认200px`
  - `min_font_size -- 字体，默认4号`
  - `max_font_size -- 根据高度自动调节`
  - `font_step -- 字体间隔，默认1`
  - `font_path -- 指定字体文件路径，默认None`
  - `max_words -- 指定词云显示的最大单词数量，默认200`
  - `stop_words -- 指定词云的排除词列表`
  - `mask -- 指定词云形状，默认长方形，需要引用imread()`
  - `background_color -- 指定词云图片背景颜色，默认黑色`
  
 

