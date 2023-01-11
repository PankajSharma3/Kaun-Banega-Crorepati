import os
import time
print("Welcome to Kaun Banega Crorepati")
print("Let's play")
while True:
    a=["Which of the following corresponds to 'ek bataa do'?","Pura","Sawa","Adha","Pauna"]
    print("Question 1:",a[0])
    print("1",a[1],"                                     ","2",a[2])
    print("3",a[3],"                                     ","4",a[4])
    b=int(input("Enter the correct option :"))
    if b==3:
        print("Congrulations, this is the correct answer")
        time.sleep(2)
        os.system('cls')
        print("You won rupees 1000")
        break
    else:
        print("OOPS, the answer is incorrect")
        print("You won rupees 0")
        print("Thanks for playing Kaun Banega Crorepati")
        break
if b==3:
    while True:
        c=["Which of the following gods is also known as 'Gauri Nandan'?","Agni","Indra","Hanuman","Ganesha"]
        print("Question 2:",c[0])
        print("1",c[1],"                                     ","2",c[2])
        print("3",c[3],"                                  ","4",c[4])
        d=int(input("Enter the correct option :"))
        if d==4:
            print("Congrulations, this is the correct answer")
            time.sleep(2)
            os.system('cls')
            print("You won rupees 2000")
            break
        else:
            print("OOPS, the answer is incorrect")
            print("You won rupees 1000")
            print("Thanks for playing Kaun Banega Crorepati")
            break
    if d==4:
        while True:
            e=["In the game of ludothe discs or tockens are ofhow many colours?","One","Two","Three","Four"]
            print("Question 3:",e[0])
            print("1",e[1],"                                     ","2",e[2])
            print("3",e[3],"                                   ","4",e[4])
            f=int(input("Enter the correct option :"))
            if f==4:
                print("Congrulations, this is the correct answer")
                time.sleep(2)
                os.system('cls')
                print("You won rupees 3000")
                break
            else:
                print("OOPS, the answer is incorrect")
                print("You won rupees 2000")
                print("Thanks for playing Kaun Banega Crorepati")
                break
        if f==4:
            while True:
                g=["Which of these are names of national paeks located in Madhya Pradesh?","Krishna and Kanhaiya","Kanha and Madhav","Ghanshyam and Murari","Girdhar and Gopal"]
                print("Question 4:",g[0])
                print("1",g[1],"                                     ","2",g[2])
                print("3",g[3],"                                     ","4",g[4])
                h=int(input("Enter the correct option :"))
                if h==2:
                    print("Congrulations, this is the correct answer")
                    time.sleep(2)
                    os.system('cls')
                    print("You won rupees 5000")
                    break
                else:
                    print("OOPS, the answer is incorrect")
                    print("You won rupees 3000")
                    print("Thanks for playing Kaun Banega Crorepati")
                    break
            if h==2:
                while True:
                    i=["Where was the BRICS summit held in 2014?","Brazil","India","Russia","China"]
                    print("Question 5:",i[0])
                    print("1",i[1],"                                     ","2",i[2])
                    print("3",i[3],"                                     ","4",i[4])
                    j=int(input("Enter the correct option :"))
                    if j==1:
                        print("Congrulations, this is the correct answer")
                        time.sleep(2)
                        os.system('cls')
                        print("You won rupees 10000")
                        break
                    else:
                        print("OOPS, the answer is incorrect")
                        print("You won rupees 5000")
                        print("Thanks for playing Kaun Banega Crorepati")
                        break
                if j==1:
                    while True:
                        k=["Who wrote the introduction to the english translation of Rabindranath Tagore's Gitanjali?","P.B. Shelley","Alfred Tennyson","W.B. Yeats","T.S. Elliot"]
                        print("Question 6:",k[0])
                        print("1",k[1],"                                     ","2",k[2])
                        print("3",k[3],"                                       ","4",k[4])
                        l=int(input("Enter the correct option :"))
                        if l==3:
                            print("Congrulations, this is the correct answer")
                            time.sleep(2)
                            os.system('cls')
                            print("You won rupees 20000")
                            break
                        else:
                            print("OOPS, the answer is incorrect")
                            print("You won rupees 10000")
                            print("Thanks for playing Kaun Banega Crorepati")
                            break
                    if l==3:
                        while True:
                            m=["Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving 2 girls from drowning?","Anandiben Patel","Vasundhara Raje Scindia","Uma Bharti","Mamata Banerjee"]
                            print("Question 7:",m[0])
                            print("1",m[1],"                                     ","2",m[2])
                            print("3",m[3],"                                          ","4",m[4])
                            n=int(input("Enter the correct option :"))
                            if n==1:
                                print("Congrulations, this is the correct answer")
                                time.sleep(2)
                                os.system('cls')
                                print("You won rupees 40000")
                                break
                            else:
                                print("OOPS, the answer is incorrect")
                                print("You won rupees 20000")
                                print("Thanks for playing Kaun Banega Crorepati")
                                break
                        if n==1:
                            while True:
                                o=["The wife of which of the famous sports person was once captian of Indian volleyball team?","K.D. Jadav","Dhayan Chand","Prakash Padukone","Milkha Singh"]
                                print("Question 8:",o[0])
                                print("1",o[1],"                                     ","2",o[2])
                                print("3",o[3],"                               ","4",o[4])
                                p=int(input("Enter the correct option :"))
                                if p==4:
                                    print("Congrulations, this is the correct answer")
                                    time.sleep(2)
                                    os.system('cls')
                                    print("You won rupees 80000")
                                    break
                                else:
                                    print("OOPS, the answer is incorrect")
                                    print("You won rupees 40000")
                                    print("Thanks for playing Kaun Banega Crorepati")
                                    break
                            if p==4:
                                while True:
                                    q=["Which of these great Indian rulers was also known by the name of 'Vikramaditya'?","Ashoka","Ajatashatru","Pushyamitra Shunga","Chandragupta II"]
                                    print("Question 9:",q[0])
                                    print("1",q[1],"                                     ","2",q[2])
                                    print("3",q[3],"                         ","4",q[4])
                                    r=int(input("Enter the correct option :"))
                                    if r==4:
                                        print("Congrulations, this is the correct answer")
                                        time.sleep(2)
                                        os.system('cls')
                                        print("You won rupees 160000")
                                        break
                                    else:
                                        print("OOPS, the answer is incorrect")
                                        print("You won rupees 80000")
                                        print("Thanks for playing Kaun Banega Crorepati")
                                        break
                                if r==4:
                                    while True:
                                        s=["The name of how many states in India begin with the english letter 'A'?","1","2","3","4"]
                                        print("Question 10:",s[0])
                                        print("1",s[1],"                                     ","2",s[2])
                                        print("3",s[3],"                                     ","4",s[4])
                                        t=int(input("Enter the correct option :"))
                                        if t==3:
                                            print("Congrulations, this is the correct answer")
                                            time.sleep(2)
                                            os.system('cls')
                                            print("You won rupees 320000")
                                            break
                                        else:
                                            print("OOPS, the answer is incorrect")
                                            print("You won rupees 160000")
                                            print("Thanks for playing Kaun Banega Crorepati")
                                            break
                                    if t==3:
                                        while True:
                                            u=["Which of these Jyotirlingas is not located in Maharashtra?","Trimbakeshwar","Omkareshwar","Ghrishneshwar","Bhimashankar"]
                                            print("Question 11:",u[0])
                                            print("1",u[1],"                                     ","2",u[2])
                                            print("3",u[3],"                                     ","4",u[4])
                                            v=int(input("Enter the correct option :"))
                                            if v==2:
                                                print("Congrulations, this is the correct answer")
                                                time.sleep(2)
                                                os.system('cls')
                                                print("You won rupees 640000")
                                                break
                                            else:
                                                print("OOPS, the answer is incorrect")
                                                print("You won rupees 320000")
                                                print("Thanks for playing Kaun Banega Crorepati")
                                                break
                                        if v==2:
                                            while True:
                                                w=["So that it is clearly visible among the debris in scenario of the crash, what is the usual colour of the 'black box'in airplanes?","Pink","Green","Orange","Blue"]
                                                print("Question 12:",w[0])
                                                print("1",w[1],"                                     ","2",w[2])
                                                print("3",w[3],"                                   ","4",w[4])
                                                x=int(input("Enter the correct option :"))
                                                if x==3:
                                                    print("Congrulations, this is the correct answer")
                                                    time.sleep(2)
                                                    os.system('cls')
                                                    print("You won rupees 1250000")
                                                    break
                                                else:
                                                    print("OOPS, the answer is incorrect")
                                                    print("You won rupees 640000")
                                                    print("Thanks for playing Kaun Banega Crorepati")
                                                    break
                                            if x==3:
                                                while True:
                                                    y=["Where is India's first 'Night Sky Sanctury' going to be set up , as per an announcement by the government in September 2022?","Ladakh","Nicobar Islands","Sunderbans","Great rann of Kutch"]
                                                    print("Question 13:",y[0])
                                                    print("1",y[1],"                                     ","2",y[2])
                                                    print("3",y[3],"                                 ","4",y[4])
                                                    z=int(input("Enter the correct option :"))
                                                    if z==1:
                                                        print("Congrulations, this is the correct answer")
                                                        time.sleep(2)
                                                        os.system('cls')
                                                        print("You won rupees 2500000")
                                                        break
                                                    else:
                                                        print("OOPS, the answer is incorrect")
                                                        print("You won rupees 1250000")
                                                        print("Thanks for playing Kaun Banega Crorepati")
                                                        break
                                                if z==1:
                                                    while True:
                                                        aa=["Which of these countries doesnot lies within close proximity of the Karakoram mountain range?","Kyrgyzstan","Tajikistan","Pakistan","Afghanistan"]
                                                        print("Question 14:",aa[0])
                                                        print("1",aa[1],"                                     ","2",aa[2])
                                                        print("3",aa[3],"                                       ","4",aa[4])
                                                        bb=int(input("Enter the correct option :"))
                                                        if bb==1:
                                                            print("Congrulations, this is the correct answer")
                                                            time.sleep(2)
                                                            os.system('cls')
                                                            print("You won rupees 5000000")
                                                            break
                                                        else:
                                                            print("OOPS, the answer is incorrect")
                                                            print("You won rupees 2500000")
                                                            print("Thanks for playing Kaun Banega Crorepati")
                                                            break
                                                    if bb==1:
                                                        while True:
                                                            cc=["Which word was added to 'Faster','Higher','Stronger', the official Olympic motto in english?","Winner","Together","Survivor","Competitor"]
                                                            print("Question 15:",cc[0])
                                                            print("1",cc[1],"                                     ","2",cc[2])
                                                            print("3",cc[3],"                                   ","4",cc[4])
                                                            dd=int(input("Enter the correct option :"))
                                                            if dd==2:
                                                                print("Congrulations, this is the correct answer")
                                                                time.sleep(2)
                                                                os.system('cls')
                                                                print("You won rupees 7500000")
                                                                break
                                                            else:
                                                                print("OOPS, the answer is incorrect")
                                                                print("You won rupees 5000000")
                                                                print("Thanks for playing Kaun Banega Crorepati")
                                                                break
                                                        if dd==2:
                                                            while True:
                                                                ee=["Which of these animals was the first to go around the moon in a spacecraft and returned to earth?","Mouse","Rabbit","Tortoise","Chimpanzee"]
                                                                print("Question 16:",ee[0])
                                                                print("1",ee[1],"                                     ","2",ee[2])
                                                                print("3",ee[3],"                                  ","4",ee[4])
                                                                ff=int(input("Enter the correct option :"))
                                                                if ff==3:
                                                                    print("Congrulations, this is the correct answer")
                                                                    time.sleep(2)
                                                                    os.system('cls')
                                                                    print("You won rupees 1 Crore")
                                                                    break
                                                                else:
                                                                    print("OOPS, the answer is incorrect")
                                                                    print("You won rupees 7500000")
                                                                    print("Thanks for playing Kaun Banega Crorepati")
                                                                    break
                                                            if ff==3:
                                                                    while True:
                                                                        gg=["Gundappa Viswanath, the first Indian to score a double century on first-class debut, achieved that feat against which team?","Services","Andhra","Maharashtra","Swarastra"]
                                                                        print("Question 17:",gg[0])
                                                                        print("1",gg[1],"                                     ","2",gg[2])
                                                                        print("3",gg[3],"                                  ","4",gg[4])
                                                                        hh=int(input("Enter the correct option :"))
                                                                        if hh==2:
                                                                            print("Congrulations, this is the correct answer")
                                                                            print("You won rupees 7 Crore")
                                                                            print("Congrulations, you are the crorepati")
                                                                            print("Thanks for playing Kaun Banega Crorepati")
                                                                            break
                                                                        else:
                                                                            print("OOPS, the answer is incorrect")
                                                                            print("You won rupees 1 Crore")
                                                                            print("Congrulations, you are the crorepati")
                                                                            print("Thanks for playing Kaun Banega Crorepati")
                                                                            break