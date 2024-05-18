# Database-Final-Project

使用方式：
1. 建立一個資料夾(這邊舉例FinalProject)，把檔案下載進那個資料夾。(不這樣做也可以，只是方便解釋)
2. 建一個虛擬環境，下載Django(底下假設虛擬環境的那個資料夾叫env)
3. 到FinalProject資料夾中，值行env\Scripts\activate啟動虛擬環境
4. 到ReactDjango裡的settings.py，把資料庫名稱和密碼改成你們自己的設定 (83~92行)
5. 把路徑改到FinalProject下，值行python manage.py runserver
6. cd frontend\frontend 之後執行 npm run build，然後npm run dev
7. 開啟瀏覽器到http://127.0.0.1:8000/
8. 我還沒寫登入和註冊，所以點登入的連結會出現錯誤
9. 他載入資料需要一點點時間，所以沒有馬上跑出東西是正常的
