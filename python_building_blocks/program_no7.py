#Read 2 string input from user, whether it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water.
print("Is it lightning there along with raining?: Yes - 0 or No - 1 ") 
answer = int(input())
if(answer == 0):
    print("Please do not go out now")
else:
    print("Then you can either choose to go out with umbrella or play with water")
