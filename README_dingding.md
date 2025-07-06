# 钉钉机器人通知工具

这是一个用于发送钉钉机器人通知的Python工具，主要用于发送工作空闲时间安排等信息。

## 功能特性

- 🤖 支持钉钉机器人Webhook发送消息
- 🔐 支持加签安全验证
- 📝 支持文本和Markdown格式消息
- 🔄 自动重试机制
- 📅 自动生成上二休二工作制的空闲时间
- 📱 支持@指定人员或@所有人
- 📊 详细的日志记录

## 安装要求

- Python 3.6+
- requests库（用于HTTP请求）

### 安装依赖
```bash
pip install requests
```

## 使用方法

### 1. 创建钉钉机器人

1. 在钉钉群中，点击右上角的群设置
2. 选择 **智能群助手** → **添加机器人**
3. 选择 **自定义** 机器人
4. 设置机器人名称和头像
5. 获取Webhook地址和加签密钥

### 2. 配置机器人信息

编辑脚本中的配置信息：

```python
# 替换为你的机器人Webhook和密钥
WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_ACCESS_TOKEN"
SECRET = "YOUR_SECRET"  # 若未启用加签则设为None
```

### 3. 运行脚本

#### 方法1：命令行运行
```bash
# 指定本月白班起始号数
python dingding_notice.py 15
```

#### 方法2：交互式运行
```bash
python dingding_notice.py
# 然后输入起始号数
```

## 功能说明

### 1. 空闲时间生成

脚本会根据上二休二工作制自动生成空闲时间段：

- **白班日**：正常工作
- **夜班日**：8:00-12:00空闲
- **休息日1**：14:00-24:00空闲
- **休息日2**：8:00-24:00空闲（全天空闲）

### 2. 消息格式

生成的消息包含：
```
1、地球aliyuntts
2、做不出来的会退费
3、可接单时间

2025年01月16日【8~12】
2025年01月17日【14~24】
2025年01月18日【8~24】
...
```

### 3. 字符数控制

- 自动控制在195字符以内
- 最多生成6个周期的时间段
- 超出限制时自动截断

## API 使用示例

### 1. 发送文本消息

```python
from dingding_notice import DingTalkRobot

# 初始化机器人
robot = DingTalkRobot(
    webhook_url="YOUR_WEBHOOK_URL",
    secret="YOUR_SECRET"
)

# 发送文本消息
robot.send_text(
    content="这是一条测试消息",
    at_mobiles=["13800138000"],  # @指定手机号
    at_all=False  # 是否@所有人
)
```

### 2. 发送Markdown消息

```python
# 发送Markdown格式消息
robot.send_markdown(
    title="每日报告",
    text="### 今日工作安排\n- 上午：会议\n- 下午：编码\n- 晚上：测试",
    at_mobiles=["13800138000"]
)
```

### 3. 生成空闲时间

```python
from dingding_notice import generate_free_time

# 生成空闲时间（从15号开始）
content = generate_free_time(15)
print(content)
```

## 配置说明

### 1. Webhook URL
- 格式：`https://oapi.dingtalk.com/robot/send?access_token=xxx`
- 从钉钉机器人设置页面获取

### 2. 加签密钥
- 用于安全验证
- 在机器人安全设置中启用加签后获取
- 如果未启用加签，设置为`None`

### 3. 重试机制
- 默认重试3次
- 每次重试间隔2秒
- 可通过`retries`参数调整

## 安全设置

### 1. 加签验证
```python
# 启用加签
robot = DingTalkRobot(
    webhook_url="YOUR_WEBHOOK_URL",
    secret="YOUR_SECRET"  # 加签密钥
)
```

### 2. IP白名单
- 在钉钉机器人设置中配置IP白名单
- 限制只有指定IP可以发送消息

### 3. 关键词限制
- 设置关键词过滤
- 只有包含关键词的消息才能发送

## 错误处理

### 1. 常见错误码
- `errcode: 0` - 发送成功
- `errcode: 130101` - 参数错误
- `errcode: 130102` - 时间戳无效
- `errcode: 130103` - 签名错误

### 2. 网络异常
- 自动重试机制
- 超时设置为5秒
- 详细的错误日志

## 日志记录

脚本会自动记录以下信息：
- 消息发送状态
- 错误信息和重试次数
- 网络异常详情

日志格式：
```
2025-01-15 10:30:00 - DingTalkRobot - INFO - 消息发送成功
2025-01-15 10:30:02 - DingTalkRobot - ERROR - 发送失败: 签名错误
```

## 使用场景

### 1. 工作安排通知
- 发送每日工作安排
- 通知空闲时间
- 提醒重要事项

### 2. 系统监控
- 服务器状态报告
- 错误告警通知
- 性能监控数据

### 3. 团队协作
- 项目进度更新
- 会议提醒
- 任务分配

## 注意事项

1. **频率限制**：钉钉机器人有发送频率限制，建议不要过于频繁
2. **内容长度**：消息内容不要过长，建议控制在2000字符以内
3. **安全设置**：建议启用加签验证，提高安全性
4. **网络环境**：确保网络连接稳定，避免发送失败

## 故障排除

### 1. 消息发送失败
- 检查Webhook URL是否正确
- 确认加签密钥是否有效
- 检查网络连接

### 2. 签名错误
- 确认时间戳是否正确
- 检查加签密钥是否匹配
- 验证签名算法

### 3. 权限问题
- 确认机器人是否被移除
- 检查群权限设置
- 验证IP白名单

## 扩展功能

### 1. 定时发送
```bash
# 使用cron定时发送
0 9 * * * cd /path/to/script && python dingding_notice.py 15
```

### 2. 集成到其他系统
```python
# 在邮件清理工具中集成
from dingding_notice import DingTalkRobot

def send_cleanup_notice(total_deleted):
    robot = DingTalkRobot(WEBHOOK_URL, SECRET)
    robot.send_text(f"邮箱清理完成，共删除{total_deleted}封邮件")
```

### 3. 自定义消息模板
```python
def generate_custom_message(data):
    return f"""
## 系统报告
- 时间：{data['time']}
- 状态：{data['status']}
- 详情：{data['details']}
    """
```

## 许可证

本项目仅供学习和个人使用，请遵守钉钉平台的使用条款。 