# ecnu_net
Login and Logout Script for SRUN Network | ECNU 网关登录脚本

## 使用说明

### 安装依赖
将仓库克隆到本地

```bash
git clone https://github.com/cubenlp/ecnu_net.git
```

安装依赖

```bash
pip install -r requirements.txt
```

根据系统情况，下载 PhantomJS

```bash
wget -c https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar -xvfj phantomjs-2.1.1-linux-x86_64.tar.bz2 && rm phantomjs-2.1.1-linux-x86_64.tar.bz2
mv phantomjs-2.1.1-linux-x86_64/ phantomjs
```

### 编辑配置文件
创建 `.env` 文件

```bash
cp .env.example .env
```

修改 `.env` 文件中的 `USERNAME` 和 `PASSWORD` 为你的学号和密码。

```bash
USERNAME=10175101234
PASSWORD=123456
```

### 运行脚本

登录校园网
```bash
./login.sh
```

登出校园网
```bash
./logout.sh
```