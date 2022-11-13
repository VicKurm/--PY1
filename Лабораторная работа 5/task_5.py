
import  random
string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
list = [1,2,3,4,5,6,7,8]
password = random.sample(string, len(list))
def get_random_password(a, n=8):
    return password

print(get_random_password(1))
