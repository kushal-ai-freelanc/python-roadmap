score=[]
for i in range(5):
    marks=float(input(f"Enter 5 subject marks {i+1}:"))
    score.append(marks)
    
print("Scores=",score)
print("Highest =",max(score))
print("lowest =",min(score))
print("Average =",(sum(score)/len(score)))