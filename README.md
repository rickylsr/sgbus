# sgbus
一个公交车到站信息和天气显示面板。

从Gov.sg获取天气，从LTA data mall获取公交数据。

## 使用
- 安装python3.10和pip
- 安装依赖：`pip install -r requirements.txt`
- 在[Land Transport Authority](https://datamall.lta.gov.sg/content/datamall/en/dynamic-data.html#Public%20Transport)申请一个API Key（秒批）
- 如果是windows，运行`Set-Variable -Name api_key -Value [你的AccountKey]`, 如果是linux，运行`export api_key [你的AccountKey]`
- `cd`到flask所在目录, 运行`flask run -p 8000 --host=0.0.0.0`
- 使用浏览器访问localhost:8000以查看面板
- 修改后请ctrl+c结束flask，重新运行flask run，否则更改有可能不生效
- 如果希望部署在生产环境，请单独配置static文件夹。

## 屏幕截图

明亮模式：

![image](https://github.com/rickylsr/sgbus/assets/10785943/efb02e48-d831-49dc-a767-bf8ea6989528)

根据时间（浏览器时间晚7-早7点）自动切换暗黑模式：

![image](https://github.com/rickylsr/sgbus/assets/10785943/b5439d72-3349-4d9f-8a74-a757749ead39)
