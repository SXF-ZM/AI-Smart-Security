# 智能园区安防视频检测系统 🚨
基于 YOLOv8 + 边缘计算 + MQTT + Web 实现的四大异常检测安防平台

## 功能清单
✅ 消防通道占用检测  
✅ 车辆滞留检测  
✅ 人员滞留检测  
✅ 围栏翻越检测  
✅ 实时告警推送  
✅ Web可视化界面  
✅ 边缘Agent自治运行  
✅ 低算力CPU可流畅运行  

## 技术栈
- Python
- YOLOv8
- OpenCV
- FastAPI
- EMQX(MQTT)
- Redis
- 边缘计算架构

## 启动方式
```bash
# 启动中心服务
python run_center.py

# 启动边缘AI检测
python run_edge.py