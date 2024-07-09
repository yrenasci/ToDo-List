tasks = []

def addTask():
    task = input("Lütfen Bir Görev Girin: ")
    tasks.append(task)
    print(f"Göreviniz '{task}' listeye eklenmiştir.")

def listTasks():
    if not tasks:
        print("Şu anda görev yok")
    else:
        print("Şu Anki Görevleriniz:")
        for index, task in enumerate(tasks):
            print(f"Görev #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Sileceğiniz # Giriniz: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Görev {taskToDelete} az önce kaldırıldı")
        else:
            print(f"Bu Görev #{taskToDelete} bulunamadı :(")
    except ValueError:
        print("Geçersiz Giriş. Sayı girmeniz gerekiyor.")
    except:
        print("Bir hata oluştu.")

if __name__ == "__main__":
    print("TO DO LIST'e Hoş Geldiniz!")
    while True:
        print("\n")
        print("Lütfen aşağıdaki seçeneklerden birini seçiniz:")
        print("----------------------")
        print("1. Yeni Görev Ekle")
        print("2. Görev Sil")
        print("3. Görev Listesini Göster")
        print("4. Çıkış")

        choice = input("Seçeneğinizi Giriniz: ")

        if choice == "1":
            addTask()

        elif choice == "2":
            deleteTask()

        elif choice == "3":
            listTasks()

        elif choice == "4":
            break
        
        else:
            print("Geçersiz Giriş. Lütfen Tekrar Deneyiniz.")

    print("Görüşmek Üzere :)")
