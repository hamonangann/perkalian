import random

print("Selamat datang di perkalian.py")

play = True
while (play):
    print("1. Main")
    print("2. Petunjuk")
    print("3. Exit")
    mode = input("Pilih (1-3): ")

    if (mode == "1"):
        lives = 3
        level = 1
        left = 1
        right = 1
        level = 1
        while (lives > 0):
            choice = random.choice(['tambah_kiri', 'tambah_kanan'])
            if (choice == 'tambah_kiri'):
                left += 1
                print("Level", level, "\nBerapa hasil dari", left, "x", right, "?")
            
                expected = str(left * right)    
                answer = input("Jawaban: ")

                if (expected == answer):
                    print("Hore benar!")
                    print("Karena", left, "x", right, "=", ((left-1) * right), "+", right, "=", (left * right), "ya!")
                else:
                    print("Yah, salah... Karena", left-1, "x", right, "=", ((left-1) * right))
                    print("Maka", left, "x", right, "=", ((left-1) * right), "+", right, "=", (left * right), "ya!")

                    lives -= 1
                    print("Sisa nyawa:", lives)
                
            else:
                right += 1
                print("Level", level, "\nBerapa hasil dari", left, "x", right, "?")
            
                expected = str(left * right)    
                answer = input("Jawaban: ")

                if (expected == answer):
                    print("Hore benar!")
                    print("Karena", left, "x", right, "=", (left * (right-1)), "+", left, "=", (left * right), "ya!")
                else:
                    print("Yah, salah... Karena", left, "x", right-1, "=", (left * (right-1)))
                    print("Maka", left, "x", right, "=", (left * (right-1)), "+", left, "=", (left * right), "ya!")

                    lives -= 1
                    print("Sisa nyawa:", lives)
            
            level += 1
            print()

        print("Game selesai. Selamat, kamu sampai level", level)

    elif (mode == "2"):
        print("Ketimbang menghafal dengan tabel, belajar perkalian lebih menyenangkan dengan latihan penjumlahan\n")

        print("Misalnya: diketahui 4 x 3 = 12, berapa hasil 5 x 3?\n")

        print("Jawab: Karena yang bertambah adalah bilangan di sebelah kiri, maka kita tambahkan hasil sebelumnya dengan bilangan di sebelah kanan")
        print("Jawabannya adalah 5 x 3 = (4 x 3) + 3 = 12 + 3 = 15\n")
        
        print("Misalnya: diketahui 5 x 2 = 10, berapa hasil 5 x 3?\n")

        print("Jawab: Nah, sekarang yang bertambah itu bilangan sebelah kanan, maka kita tambahkan hasil sebelumnya dengan bilangan sebelah kiri")
        print("Jangan sampai terbalik ya!")
        print("Jadi jawabannya adalah 5 x 3 = (5 x 2) + 5 = 10 + 5 =15\n")

    elif (mode == "3"):
        play = False
    
    else:
        print("Ketik angka pilihanmu ya...")

    print()

print("Bye-bye!")