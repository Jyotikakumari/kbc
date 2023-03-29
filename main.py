print("................WELCOME IN KBC GAME....................")
input("press enter to start game")

q1 ="which city is known as pink city?"
q2 ="who is the father of the computer?"
q3 ="who is the inovator of optics?"
q4 ="who is the father of the nation?"
q5 ="which city is a cleanest city in india?"
Score=0

print("q1)",q1)
print("a. Purnea\t b. Jaipur\nc. Bhopal\t d.none of these")
ans = input("type a/b/c/d for answer")
Score+=20000
if ans=='b'or ans=='B':
    print("wow..Right Answer",Score)
    print("q2)",q2)
    print("a. Rahul kumar\t b.Dhoni\nc.Charles Babbage\t d.none of these")
    ans=input("type a/b/c/d for answer")
    Score+=30000
    if ans =='c'or ans=='C':
        print("wow..right answer",Score)
        print("q3)",q3)
        print("a.Ibn Al-Haytham\t b.Ibn rahul\nc.Anurag\t d.None of these")
        ans=input("type a/b/c/d for answe")
        Score+=40000
        if ans=='a' or ans=='A':
            print("wow..right answer",Score)
            print("q4)",q4)
            print("a.Salman Khan\t b.Ajay Devgan\nc.Mahatma Gandhi\t d. none of these")
            ans=input("type a/b/c/d for answer")
            Score+=50000
            if ans=='c'or ans=='C':
                print("wow..right answer",Score)
                print("q5)",q5)
                print("a.Purnea\t b.Bhagalpur\nc.Katihar\t d.Indore")
                ans=input("type a/b/c/d for answer")
                Score+=60000
                if ans=='d'or ans=='D':
                    print("Finally you are Winner",Score)
                else:
                    print("wrong answer")    
            else:
                print("wrong answer")    
        else:
            print("wrong answer")    
    else:
        print("wrong answer")

else:
    print("sorry Wrong answer")    
