from konlpy.tag import Hannanum,Kkma, Okt
import tkinter as tk

def morph():
    hannanum = Hannanum()
    txt = ent.get()
    output = hannanum.morphs(txt)

    result.configure(text=str(output))

def noun():
    hannanum = Hannanum()
    txt = ent.get()
    output = hannanum.nouns(txt)

    result.configure(text=str(output))

def pos():
    hannanum = Hannanum()
    txt = ent.get()
    output = hannanum.pos(txt)

    result.configure(text=str(output))



window = tk.Tk()

window.configure(bg='pink')
window.geometry('1000x1000')

lab=tk.Label(window, text="문장/단어를 입력하세요", width=20, height=1, font=('맑은 고딕',16,'bold'), bg='pink', fg='black')
lab.place(x=360, y=100)
taglist='E: 어미, EC: 연결 어미, EF: 종결 어미, EP: 선어말어미, ET: 전성 어미, F: 외국어, \nI: 독립언, II: 감탄사, J: 관계언, JC: 격조사, JP: 서술격 조사, JX: 보조사,\nM: 수식언, MA: 부사, MM: 관형사, N: 체언, NB: 의존명사, NC: 보통명사,\nNN: 수사, NP: 대명사, NQ: 고유명사, P: 용언, PA: 형용사, PV: 동사, \nPX: 보조 용언, S: 기호, X: 접사, XP: 접두사, XS: 접미사'
lab1=tk.Label(window, text=taglist, width=100, height=5, font=('맑은 고딕',8,'bold'), bg='pink', fg='black')
lab1.place(x=120, y=300)
result=tk.Label(window, width=150, height=1, font=('맑은 고딕',10,'bold'), bg='pink', fg='green')
result.place(x=-110, y=700)

ent=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=60)
ent.place(x=130, y=200)

button1 = tk.Button(window,text='형태소 분석',font=('맑은 고딕',16,'bold'),bg="red",fg='white',width=10,command=morph) 
button1.place(x=50,y=400)
button2 = tk.Button(window,text='명사 추출',font=('맑은 고딕',16,'bold'),bg="red",fg='white',width=10,command=noun) 
button2.place(x=400,y=400)
button3 = tk.Button(window,text='품사 정보',font=('맑은 고딕',16,'bold'),bg="red",fg='white',width=10,command=pos) 
button3.place(x=800,y=400)


window.mainloop()

    