# Database-Final-Project

使用方式：
1. 建立一個資料夾(這邊舉例FinalProject)，把檔案下載進那個資料夾。(不這樣做也可以，只是方便解釋)
2. 建一個虛擬環境，下載Django(底下假設虛擬環境的那個資料夾叫env)
3. 到FinalProject資料夾中，值行env\Scripts\activate啟動虛擬環境
4. 到ReactDjango裡的settings.py，把資料庫名稱和密碼改成你們自己的設定 (83~92行)
5. 把路徑改到FinalProject下，值行python manage.py makemigrations, python manage.py migrate更新資料表
6. 之後值行python manage.py runserver啟動server
7. cd frontend\frontend 之後執行 npm run build，然後npm run dev
8. 開啟瀏覽器到http://127.0.0.1:8000/
9. 我還沒寫登入和註冊，所以點登入的連結會出現錯誤
10. 他載入資料需要一點點時間，所以沒有馬上跑出東西是正常的
