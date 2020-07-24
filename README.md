# MCDR-WebRemoter
MCDR-WebRemoter是一款可以让你在网页端控制MC服务器的插件。所有危险操作都使用了 ` HTTP Basic Authentication ` 保证您服务器的安全

# 安装
1. 将本仓库直接复制到MCDR的plugins文件夹中 **注意不要改变文件的相对位置**

2. 复制完后，在plugins文件夹中运行 ` pip3 install -r requirement.txt `
3. 依照代码中的注释设置 ` WebServer.py ` 中的 ` users ` 列表
4. 允许python通过系统防火墙

安装完成

# 配置

在 ` WebRemoter.py ` 中：

- ` serverPort ` --> Web服务器的运行端口，应与 ` WebServer.py ` 中的 ` httpPort ` 属性统一
- ` executeInterval ` --> 决定MCDR多久向服务器请求一次命令 数值越小相应越快，数值越大占资源越少
  


在 ` WebRemoter.py ` 中：
- ` httpPort ` --> Web服务器的运行端口，应与 ` WebRemoter.py ` 中的 ` serverPort ` 属性统一
- ` users ` --> 用户控制，请按照注释示例设置

# 使用
使用浏览器访问您的域名/IP地址，并在弹出的密码框中输入 `WebRemoter.py ` 文件中 ` users ` 设定的用户名即可正常使用