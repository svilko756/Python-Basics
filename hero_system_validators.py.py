def hero_name(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        if not x.find(" ") == -1:
           return "Sorry the username can't contain spaces"
        elif not ( x.find("@") or x.find("#") or x.find("$"))   == -1:
           return "Sorry the username can't contain specific symbols"
        elif len(x) < 5  or len(x)> 13:
           return "Sorry your username isn't enough good with characters"
        else:
            return f"Hello {x}"
    return wrapper

def double_strenght(func):
    def wrapper(*args, **kwargs):   
       result = func(*args, **kwargs)
       power = args[0]
       new_power = power * 2
       return f"Your strenght has doubled for {new_power}"
    return wrapper

def check_stamina(func):
    def wrapper(*args, **kwargs):
         result = func(*args, **kwargs)
         if result < 20:
             print("Your stamina is very low you need to rest")
             return result
         else:
             print("Your stamina is enough for battle")
             return result
    return wrapper

def critical_hit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 50:
           enemy = input("What is your enemy you want to deal with: ")
           skill = input("What skill wii you use againts your enemy: ")
           return f"You are fighting {enemy} and you will use {skill} to defeait it"
        else:
           return f"You don't have enough skill ponts to fight with enemy"
    return wrapper

@hero_name
def hero(name):
    return name

@double_strenght
def hero_strenght(points):
    return points
@check_stamina
def stamina(points):
    return points

@critical_hit
def skill(point):
    return point

print(hero("Svilen"))
print(hero_strenght(100))
print(stamina(15))
print(skill(20))
