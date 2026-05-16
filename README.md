# 智能园区安防视频检测系统（AI+边缘计算）
基于 YOLOv8+DeepSORT+EMQX+Redis+FastAPI 构建的边缘-中心分布式安防系统，实现消防通道占用、车辆滞留、人员翻越围栏、人员滞留四大智能检测功能，支持实时告警、远程可视化、边缘自治、故障自愈，适配园区、小区、车库安防场景。

## 项目亮点
- ✅ **边缘计算架构**：检测推理下沉边缘节点，低延迟、低带宽占用
- ✅ **四大核心检测**：消防通道占用、车辆滞留、人员翻越、人员滞留
- ✅ **轻量化部署**：YOLOv8n/s+ONNX加速，CPU/嵌入式设备可运行
- ✅ **EMQX(MQTT)消息总线**：异步解耦、高可靠、支持弱网
- ✅ **Agent 智能代理**：边缘自治、配置缓存、故障自愈、算力调度
- ✅ **全链路工程化**：Docker容器化、Redis配置中心、Web可视化、告警推送

## 技术栈
### 边缘端
- 视频流：FFmpeg + OpenCV（RTSP拉流）
- AI检测：YOLOv8（人/车检测）
- 目标跟踪：DeepSORT（轨迹关联、ID稳定）
- 推理加速：ONNX Runtime（FP16量化，提速2-5倍）
- 消息通信：EMQX(MQTT)
- 智能代理：Agent（Python+Redis）

### 中心端
- 信号服务：FastAPI
- 可视化：WebSocket实时推送
- 配置管理：Redis
- 数据存储：MySQL（可扩展）

## 项目结构
smart_security/
├── agent/ # Agent 智能代理（调度 / 自愈 / 缓存）
├── m01_stream/ # M01 RTSP 视频流接入
├── m02_detect/ # M02 YOLOv8+DeepSORT 检测 + 规则
├── m03_signal/ # M03 EMQX 信号服务
├── m04_web/ # M04 FastAPI Web 可视化
├── m05_config/ # M05 Redis 配置管理
├── common/ # 公共工具
├── config/ # ROI / 阈值 / 白名单
├── media/ # 异常截图 / 视频
├── run_edge.py # 边缘启动入口
└── run_center.py # 中心启动入口

## 环境安装
```bash
# 虚拟环境
python -m venv venv
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

快速启动
1. 启动中心（Web+Redis）
python run_center.py
2. 启动边缘（Agent + 检测）
python run_edge.py

3. Web 可视化
浏览器访问：http://localhost:8000
核心功能说明
F01 消防通道占用检测
检测黄色网格线区域车辆违停
判定：车辆停留≥5 分钟，非白名单
输出：is_abnormal=1，车辆数量、占用时长
F02 车辆滞留检测
车库出入口、连廊等非正规停车区
分区域阈值（出入口 3 分钟、连廊 10 分钟）
白名单过滤（消防车、救护车）
F03 人员翻越围栏检测
周界围栏非法翻越
双警戒线轨迹判定，秒级告警
紧急级别：emergency
F04 人员滞留检测
围栏危险区域长时间逗留
分时段灵敏度：夜间阈值减半
输出：滞留时长、时段类型、灵敏度
性能优化
模型轻量化：YOLOv8n/s，算力消耗低
ONNX 量化：FP16，推理提速 2-5 倍
ROI 过滤：仅检测关注区域，减少无效推理
动态降帧：无人无车 15fps，有目标 30fps
边缘缓存：网络抖动缓存 10s 帧，防漏检
部署方式
Docker 一键部署
docker-compose up -d

硬件适配
边缘：Jetson Orin、工控机、嵌入式设备
系统：Ubuntu、麒麟 OS、统信 UOS
摄像头：海康、大华、宇视（RTSP 协议）
项目价值
工程化完整：从需求→设计→开发→部署→运维全流程
技术栈主流：AI 检测、边缘计算、消息队列、Web 开发
可直接落地：适配真实园区安防场景，可商用部署
简历硬核：完整 AI + 工程化项目，面试高含金量