import subprocess
import random as r
class Ipchanger:
    @staticmethod
    def change_random():
        cmd =f'netsh interface ipv4 set address name="Wi-Fi" static {r.randint(1,256)}.{r.randint(1,256)}.{r.randint(1,256)}.{r.randint(1,256)} 255.255.255.0  {r.randint(1,256)}.{r.randint(1,256)}.{r.randint(1,256)}.{r.randint(1,256)} '.split()
        result = subprocess.run(cmd, capture_output= True,
                        text=True)                              
        result = result.stdout
        return result
    @staticmethod
    def change_default():
        cmd ='netsh interface ipv4 set address name="Wi-Fi" static 192.168.0.107 255.255.255.0 192.168.0.1'.split()

        result = subprocess.run(cmd, capture_output= True,
                                text=True)                              
        result = result.stdout

        return result

if __name__=="__main__":
    k = Ipchanger()
    h = input()
    if h=='1':
        k.change_random()
    # result = subprocess.run(['ipconfig'], capture_output=True, text=True)
    if h=='0':
        k.change_default()
    # print(result.stdout)
    