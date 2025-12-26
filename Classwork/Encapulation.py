class Instagram:
    def __init__(self,username,pwd):
        print("Welcome to the instagram. Have a fun!!!")
        self.username = username
        self.__password = pwd
        self._post=[]

    def getPassword(self):
        return self.__password
    
    def setPassword(self,newPassword):
        self.__password=newPassword
        print("Password updated")
        
    @property
    def viewPost(self):
        return self._post
    
    @viewPost.setter
    def viewPost(self,post):
        self._post.append(post)

randheer=Instagram("Randheer","r@123")
print(f"Before: {randheer.username}")
randheer.username="Sumanth"
print(f"After: {randheer.username}")

print(f"Before: {randheer.getPassword()}")
randheer.setPassword("Sumanth@123")
print(f"After: {randheer.getPassword()}")

print(randheer.viewPost)
randheer.viewPost="hello"
randheer.viewPost="First Reel"
print(randheer.viewPost)