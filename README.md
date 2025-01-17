# 全國土地使用分區GeoJSON
- [專案說明](#專案說明)
- [資料說明](#資料說明)
- [操作說明](#操作說明)
- [專案結構](#專案結構)

## 專案說明
本專案為為下載全國土地使用分區GeoJSON檔而設計之極簡易網頁，使用python的flask框架進行架設，詳細網站內容可以參考以下連結。

- [Demo影片](https://youtu.be/HBMdp_R6kuI)
- [Medium文章分享](https://medium.com/@godspeed_huang/%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%E5%88%86%E5%8D%80%E5%9C%96%E8%B3%87%E5%8F%96%E5%BE%97-b0a80774c9b2)


## 資料說明
本網站之土地使用分區資料座標系統為`TWD97`，且資料非即時資料，其最後更新年份為`民國109年`，請斟酌使用，本網站所有資料皆不得作為任何形式證明或主張，最新資料請以政府網站為準。

## 操作說明
### 1. 網站初始畫面 
![初始畫面](/images/01.png)
### 2. 選擇`縣市`與`都計區`名稱後，點擊`下載`。
![操作畫面](/images/02.png)
### 3. 網頁將會跳轉到GeoJSON檔案頁面，點擊右鍵`另存新檔`。
![檔案畫面](/images/03.png)
### 4. GeoJSON檔可於GIS軟體中作為`向量檔案`開啟，並可再依需求做座標與檔案格式(.shp/.dxf等)轉換。
![GIS畫面](/images/04.png)
### 5. 若網頁無法開啟，可於`static`資料夾找到全國土地使用分區GeoJSON檔案，並根據`preprocess`中的`county_district`資料夾找到各土地使用分區對應之代碼，並下載之。


## 專案結構
```
landuse_GeoJSON_web/
    ├─ preprocess/
    |   ├─ county.py             // 獲取縣市代碼
    |   ├─ sectors.py            // 獲取各縣市計畫區代碼
    |   ├─ taiwan_administrative_disions.csv
    |   └─ county_district/
    |       └─ 計畫區代碼與名稱對照檔
    ├─ static/
    |   └─ 全國土地使用分區GeoJson檔
    ├─ templates/
    |   ├─ index.html            // 主網頁
    |   ├─ js/
    |   └─ style/
    ├─ app.py                    // 主程式
    ├─ requirements.txt          
    ├─ runtime.txt
    ├─ Procfile
    ├─ images/        
    └─ README.md    
```