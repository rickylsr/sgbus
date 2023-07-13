# sgbus
一个公交车到站信息面板。
## 使用
- 安装python3.10和pip
- `pip install requests flask`
- 在[Land Transport Authority](https://datamall.lta.gov.sg/content/datamall/en/dynamic-data.html#Public%20Transport)申请一个API Key（秒批）
- 如果是windows，运行`Set-Variable -Name api_key -Value [你的AccountKey]`, 如果是linux，运行`export api_key [你的AccountKey]`
- `cd`到flask所在目录, 运行`flask run -p 8000 --host=0.0.0.0`
- 使用浏览器访问localhost:8000以查看面板
- 修改后，请ctrl+c结束flask后，重新运行flask run
