#1
print("---Task1---")
def find_and_print(messages):
# write down your judgment rules in comments
# rule1: 18>17 (older than 17)
#  rule2: college student (probably older than 18, but there's someone who skips a grade)
#  rule3: legal age in Taiwan (age:18)
#  rule4: vote in U.S.A (age:18)
# your code here, based on your own rules

    namelist=messages.keys()
    for x in namelist:
        if messages[x].find("18 years old.") != -1 :
            print(x)
        elif messages[x].find("legal age in Taiwan") != -1 :
            print(x)
        elif messages[x].find("vote for Donald Trump") != -1 :
            print(x)
    
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.", 
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.", "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week", "Jenny":"Good morning."
})

#2
print("---Task2---")

def calculate_sum_of_bonus(data):
# write down your bonus rules in comments
# bonus = salary *s *p 
# s depends on salary range (salary higher than 40000, s=1.05 ; salary lower than 40000, s = 1.1)
# p depends on performance (above average, p=1.05 ; averge, p=1.02 ; below average, p=1)

# your code here, based on your own rules
    #format salary type
    workers = data["employees"]
    for x in workers:
        #remove ,
        if type(x["salary"]) == str:
            x["salary"] = x["salary"].replace(",","")
        #change USD to TWD
        if type(x["salary"]) == str and x["salary"].find("USD") != -1:
            x["salary"] = x["salary"].replace("USD","")
            x["salary"] = int(x["salary"])*30
        #make sure they're all int not string
        x["salary"] = int(x["salary"])
    
    s=0
    p=0
    sum_of_bonus = 0
    for x in workers:
        if x["salary"] >= 40000:
            s=1.05
        else:
            s=1.1
        if x["performance"] == "above average":
            p=1.05
        elif x["performance"] == "average":
            p=1.02
        else:
            p=1
        sum_of_bonus += int(x["salary"]*s*p)
    print(sum_of_bonus)
    
calculate_sum_of_bonus({ 
    "employees":[
        {
            "name":"John",
            "salary":"1000USD", 
            "performance":"above average", 
            "role":"Engineer"
        }, 
        {
            "name":"Bob", 
            "salary":60000, 
            "performance":"average", 
            "role":"CEO"
        }, 
        {
            "name":"Jenny", 
            "salary":"50,000", 
            "performance":"below average", 
            "role":"Sales"
        } 
    ]
}) # call calculate_sum_of_bonus function

#3
print("---Task3---")

def func(*data):
# your code here
    namelist = list(data)
    middle_name = []
    result = ""
    for x in data:
        middle_name.append(x[1:2])
    for y in middle_name:
        if middle_name.count(y) == 1:
            result = namelist[middle_name.index(y)]
            print(result)

    if result == "":
        print("沒有")

func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

#4
print("---Task4---")
#JS寫完有先諮詢助教，助教建議這題可以試著用迴圈寫，而不是數學運算，因此在python試著使用迴圈完成任務。。
def get_number(index):
    result = 0
    for x in range(1,index+1):
        if index == 0:
            print(result)
            break
        elif x%2 == 1:
            result += 4
        elif x%2 == 0:
            result -= 1
    print(result)
        
# your code here 
get_number(1) # print 4
get_number(5) # print 10 
get_number(10) # print 15
