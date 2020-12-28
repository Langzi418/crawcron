本地数据库名为 military_multimode。  
所有数据存在一张表spider_article。

通过conf.json文件完成前后端交互，
后端定时爬取数据库，插入数据库并更新conf.json文件
例如：
```json
{
  "updated": 34,// 截至目前为止，总的更新数据量
  "src": {
    // 每个数据源更新的数据量
    "jiqizhixin": {
      "last": "1608647358.403068",// 最后更新时间
      "updated": 12// 更新数据量
    },
    "qbitai": {
      "last": "1608647358.403068",
      "updated": 8
    },
    "AItists": {
      "last": "1608647358.403068",
      "updated": 8
    },
    "elecfans": {
      "last": "1608651965.5096123",
      "updated": 6
    }
  }
}
```


前端通过定时访问后端接口来消费更新的数据。
后端接口是通过访问conf.json文件来感知数据的更新。

一些人工智能数据源  
https://www.jiqizhixin.com/
https://www.qbitai.com/
https://www.wxnmh.com/user-5423.htm
https://wemp.app/accounts/973991ad-c4de-49a4-a553-96c286116b4b
https://wemp.app/accounts/94cf1960-e31f-4da3-9914-90dd9528a3fe
https://wemp.app/accounts/9347d7b4-e4a1-4a3a-8231-c399c5aa4e0a