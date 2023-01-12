import time
import os
a=[["Which of the following corresponds to 'ek bataa do'?","Pura","Sawa","Adha","Pauna","3"],["Which of the following gods is also known as 'Gauri Nandan'?","Agni","Indra","Hanuman","Ganesha","4"],["In the game of ludo the discs or tockens are of how many colours?","One","Two","Three","Four","4"],["Which of these are names of national paeks located in Madhya Pradesh?","Krishna and Kanhaiya","Kanha and Madhav","Ghanshyam and Murari","Girdhar and Gopal","2"],["Where was the BRICS summit held in 2014?","Brazil","India","Russia","China","1"],["Who wrote the introduction to the english translation of Rabindranath Tagore's Gitanjali?","P.B. Shelley","Alfred Tennyson","W.B. Yeats","T.S. Elliot","3"],["Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving 2 girls from drowning?","Anandiben Patel","Vasundhara Raje Scindia","Uma Bharti","Mamata Banerjee","1"],["The wife of which of the famous sports person was once captian of Indian volleyball team?","K.D. Jadav","Dhayan Chand","Prakash Padukone","Milkha Singh","4"],["Which of these great Indian rulers was also known by the name of 'Vikramaditya'?","Ashoka","Ajatashatru","Pushyamitra Shunga","Chandragupta II","4"],["The name of how many states in India begin with the english letter 'A'?","1","2","3","4","3"],["Which of these Jyotirlingas is not located in Maharashtra?","Trimbakeshwar","Omkareshwar","Ghrishneshwar","Bhimashankar","2"],["So that it is clearly visible among the debris in scenario of the crash, what is the usual colour of the 'black box'in airplanes?","Pink","Green","Orange","Blue","3"],["Where is India's first 'Night Sky Sanctury' going to be set up , as per an announcement by the government in September 2022?","Ladakh","Nicobar Islands","Sunderbans","Great rann of Kutch","1"],["Which of these countries doesnot lies within close proximity of the Karakoram mountain range?","Kyrgyzstan","Tajikistan","Pakistan","Afghanistan","1"],["Which word was added to 'Faster','Higher','Stronger', the official Olympic motto in english?","Winner","Together","Survivor","Competitor","2"],["Which of these animals was the first to go around the moon in a spacecraft and returned to earth?","Mouse","Rabbit","Tortoise","Chimpanzee","3"],["Gundappa Viswanath, the first Indian to score a double century on first-class debut, achieved that feat against which team?","Services","Andhra","Maharashtra","Swarastra","2"]]
b=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,"1 Crore","7 Crore"]
e=[0,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,"1 Crore"]
d=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
for i in range(0,len(a)):
    print(f"Question {i+1} : {a[i][0]}")
    print(f"1. {a[i][1]}")
    print(f"2. {a[i][2]}")
    print(f"3. {a[i][3]}")
    print(f"4. {a[i][4]}")
    c=(input("Enter your answer : "))
    if c==a[i][5]:
        print("Congratulations, this is the correct answer")
        time.sleep(1)
        os.system('cls')
        print("  ")
        print(f"You won {b[i]} rupees")
    else:
        print("OOPS, the answer is incorrect")
        print(f"The total amount won by you is {e[i]} rupees")
        break
print("Thanks for playing Kaun Banega Crorepati")