#1.POLYMORPHISM

class Hotstar:
    def playvideo(self):
        print("Movie with ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("One device login")
        print("No download option")
        print("No live access")
        print("Sound quality")

    def playvideo(self,premium):
        print("Movie with ads")
        print("Unlimited access for movies")
        print("High quality")
        print("Multiple device login")
        print("Download option is avaliable")
        print("Live access")
        print("Improved sound quality")

Leela=Hotstar()
Leela.playvideo("Leela")

#2.METHOD OVERRIDING

class Hotstar:
    def __init__(self,username):
        print(f"Hi{username} Welcome to the Hostar".center(40,'-'))
    def playvideo(self):
        print("Movie with ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("One device login")
        print("No download option")
        print("No live access")
        print("Sound quality")

    def login(self):
        print("Login is same")
    def interface(self):
        print("Same interface")
    def profile(self):
        print("Profile is same")
class premiumUser(Hotstar):
    def __init__(self,username):
        print(f"Hi{username} Welcome to the Hostar.Enjoy the premium".center(60,'-'))
    def playvideo(self):
        print("Movie with ads")
        print("Unlimited access for movies")
        print("High quality")
        print("Multiple device login")
        print("Download option is avaliable")
        print("Live access")
        print("Improved sound quality")

Leela=Hotstar("Leela")
Leela.playvideo()
Leela.login()

bhavani=premiumUser("Bhavani")
bhavani.playvideo()
bhavani.login()

#3.METHOD OVERRIDING-2

class Instagram:
    def feed(self):
        print("Feed is same for all")
    def scrolling(self):
        print("Scrolling is same for all")
    def share(self):
        print("Sharing is same for all")
    def like(self):
        print("Like is same for all")
    def repost(self):
        print("repost is same for all")
    def comment(self):
        print("comment is same for all")
    def profile(self):
        print("No professional dashboard")
    def posting(self):
        print("No insights are availabale")

class creator(Instagram):
    def profile(self):
        print("Professional dashboard is adding in their grid")
    def post(self):
        print("You can see the reach,profile activities,followers")

chintu=creator()
chintu.profile()
chintu.posting()

pandu=Instagram()
pandu.profile()
pandu.posting()
