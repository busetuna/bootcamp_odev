
class task:
    def __init__(self , gorevAdi , Durum):
        self.gorevAdi = gorevAdi
        self.Durum = Durum
        
    def __str__(self):
        return f"{self.gorevAdi} - {self.Durum}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def ekle(self, gorev):
        self.tasks.append(gorev)
        with open("odev_dosya.txt", "a") as dosya:
            dosya.write(f"Görev eklendi : {gorev}\n")
        
    
    def sil(self, gorev):
        if gorev in self.tasks:
            self.tasks.remove(gorev)
            with open("odev_dosya.txt" , "a") as dosya:
                dosya.write(f"Görev silindi : {gorev}\n")
            

    def yonet(self):
        with open("odev_dosya.txt" , "a") as dosya:
            dosya.write(f"Görev listesi: \n")
            for i , gorev in enumerate(self.tasks , start=1):
                dosya.write(f"{i}. {gorev}\n")
            
        

if __name__ == "__main__":
    manager =TaskManager()

    gorev1 = task("python odevi" , "tamamlandı")
    gorev2 = task("java odevi" , "tamamlanmadi")

    manager.ekle(gorev1)

    manager.sil(gorev1)

    manager.yonet()
    
