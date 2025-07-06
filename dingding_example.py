#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
钉钉机器人通知工具 - 使用示例
演示如何使用钉钉机器人发送各种类型的消息
"""

from dingding_notice import DingTalkRobot, generate_free_time

def example_usage():
    """使用示例"""
    print("钉钉机器人通知工具 - 使用示例")
    print("=" * 50)
    
    # 配置信息（请替换为您的实际配置）
    WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_ACCESS_TOKEN"
    SECRET = "YOUR_SECRET"  # 若未启用加签则设为None
    
    print("请先配置您的钉钉机器人信息：")
    print(f"Webhook URL: {WEBHOOK_URL}")
    print(f"Secret: {SECRET}")
    print("\n注意：请将上述配置替换为您的实际配置信息")
    
    # 示例1：发送简单文本消息
    print("\n=== 示例1: 发送简单文本消息 ===")
    try:
        robot = DingTalkRobot(WEBHOOK_URL, SECRET)
        success = robot.send_text("这是一条测试消息")
        if success:
            print("✅ 文本消息发送成功")
        else:
            print("❌ 文本消息发送失败")
    except Exception as e:
        print(f"❌ 发送失败: {str(e)}")
    
    # 示例2：发送@指定人的消息
    print("\n=== 示例2: 发送@指定人的消息 ===")
    try:
        robot = DingTalkRobot(WEBHOOK_URL, SECRET)
        success = robot.send_text(
            content="请查看最新的工作安排",
            at_mobiles=["13800138000"],  # 替换为实际手机号
            at_all=False
        )
        if success:
            print("✅ @指定人消息发送成功")
        else:
            print("❌ @指定人消息发送失败")
    except Exception as e:
        print(f"❌ 发送失败: {str(e)}")
    
    # 示例3：发送Markdown格式消息
    print("\n=== 示例3: 发送Markdown格式消息 ===")
    try:
        robot = DingTalkRobot(WEBHOOK_URL, SECRET)
        markdown_text = """
### 今日工作安排
- **上午**: 团队会议
- **下午**: 项目开发
- **晚上**: 代码审查

### 重要提醒
> 请及时更新项目进度
> 注意代码质量

[查看详细安排](http://example.com)
        """
        success = robot.send_markdown(
            title="每日工作安排",
            text=markdown_text
        )
        if success:
            print("✅ Markdown消息发送成功")
        else:
            print("❌ Markdown消息发送失败")
    except Exception as e:
        print(f"❌ 发送失败: {str(e)}")
    
    # 示例4：生成并发送空闲时间
    print("\n=== 示例4: 生成并发送空闲时间 ===")
    try:
        # 生成空闲时间（从15号开始）
        free_time_content = generate_free_time(15)
        print("生成的空闲时间内容:")
        print(free_time_content)
        
        robot = DingTalkRobot(WEBHOOK_URL, SECRET)
        success = robot.send_text(free_time_content)
        if success:
            print("✅ 空闲时间消息发送成功")
        else:
            print("❌ 空闲时间消息发送失败")
    except Exception as e:
        print(f"❌ 发送失败: {str(e)}")
    
    # 示例5：发送系统监控报告
    print("\n=== 示例5: 发送系统监控报告 ===")
    try:
        robot = DingTalkRobot(WEBHOOK_URL, SECRET)
        monitor_text = """
### 系统监控报告
**时间**: 2025-01-15 10:30:00

**服务器状态**:
- CPU使用率: 65%
- 内存使用率: 78%
- 磁盘使用率: 45%
- 网络状态: 正常

**告警信息**:
- 无严重告警
- 系统运行正常

**建议操作**:
- 定期清理日志文件
- 监控内存使用趋势
        """
        success = robot.send_markdown(
            title="系统监控报告",
            text=monitor_text
        )
        if success:
            print("✅ 监控报告发送成功")
        else:
            print("❌ 监控报告发送失败")
    except Exception as e:
        print(f"❌ 发送失败: {str(e)}")

def test_free_time_generation():
    """测试空闲时间生成功能"""
    print("\n=== 测试空闲时间生成 ===")
    
    # 测试不同的起始日期
    test_dates = [1, 15, 30]
    
    for start_day in test_dates:
        print(f"\n从{start_day}号开始的工作安排:")
        try:
            content = generate_free_time(start_day)
            print(content)
            print(f"字符数: {len(content)}")
        except Exception as e:
            print(f"生成失败: {str(e)}")

def main():
    """主函数"""
    print("钉钉机器人通知工具 - 功能演示")
    print("=" * 50)
    
    print("请选择要演示的功能:")
    print("1. 完整功能演示（需要配置机器人信息）")
    print("2. 仅测试空闲时间生成")
    print("3. 退出")
    
    choice = input("\n请输入选择 (1-3): ").strip()
    
    if choice == '1':
        example_usage()
    elif choice == '2':
        test_free_time_generation()
    elif choice == '3':
        print("退出程序")
    else:
        print("无效选择")

if __name__ == "__main__":
    main() 