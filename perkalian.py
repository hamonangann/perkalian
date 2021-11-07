import random

print("Selamat datang di perkalian.py")

play = True
while (play):
    print("1. Main!")
    print("2. Trik rahasia!")
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
                    # print("Karena", left, "x", right, "=", ((left-1) * right), "+", right, "=", (left * right), "ya!")
                else:
                    print("Yah, salah... yang benar adalah", expected, "ya!") #Karena", left-1, "x", right, "=", ((left-1) * right))
                    # print("Maka", left, "x", right, "=", ((left-1) * right), "+", right, "=", (left * right), "ya!")

                    lives -= 1
                    print("Sisa nyawa:", lives)
                
            else:
                right += 1
                print("Level", level, "\nBerapa hasil dari", left, "x", right, "?")
            
                expected = str(left * right)    
                answer = input("Jawaban: ")

                if (expected == answer):
                    print("Hore benar!")
                    # print("Karena", left, "x", right, "=", (left * (right-1)), "+", left, "=", (left * right), "ya!")
                else:
                    print("Yah, salah... yang benar adalah", expected, "ya!") # Karena", left, "x", right-1, "=", (left * (right-1)))
                    # print("Maka", left, "x", right, "=", (left * (right-1)), "+", left, "=", (left * right), "ya!")

                    lives -= 1
                    print("Sisa nyawa:", lives)
            
            level += 1
            print()

        print("Game selesai. Selamat, kamu sampai level", level, "!")

    elif (mode == "2"):
        print(20*('='), "TRIK RAHASIA", 20*('='))
        print("Rahasia game ini (dan juga perkalian pada dunia nyata): perkalian adalah penjumlahan berulang!")
        print("Sebagai contoh, 3 x 4 = 4 + 4 + 4 (4-nya ada 3) = 12. Bisa juga 3 x 4 = 3 + 3 + 3 + 3 (3-nya ada 4) = 12")
        print()

        print("Nah, dengan memerhatikan jawaban soal sebelumnya, kamu bisa menjawab pertanyaan lebih cepat!")
        print("Misalnya, sebelumnya ditanyakan 2 x 5 = 10")
        print()

        print("Kalau kamu ditanya berapa 3 x 5, maka ingat bahwa 2 x 5 itu 5-nya 2 kali, sedangkan 3 x 5 itu 5-nya 3 kali")
        print("Artinya, karena 2 x 5 = 5 + 5, maka 3 x 5 = 5 + 5 + 5 = (2 x 5) + 5 = 10 + 5")
        print("Jadi, kamu hanya perlu menambahkan 5 dari jawaban sebelumnya, sehingga didapatlah hasil 3 x 5 = 15")
        print()

        print("Nah, kalau kamu ditanya berapa 2 x 6, maka ingat 2 x 5 itu 2-nya 5 kali, sedangkan 2 x 6 itu 2-nya 6 kali")
        print("Mirip tadi, karena 2 x 5 = 2 + 2 + 2 + 2 + 2, maka 2 x 6 = 2 + 2 + 2 + 2 + 2 + 2 = (2 x 5) + 2 = 10 + 2")
        print("Jadi, kamu hanya perlu menambahkan 2 dari jawaban sebelumnya, sehingga hasilnya adalah 2 x 6 = 12")
        print()

        print(20*('='), "Good luck!", 20*('='))

    elif (mode == "3"):
        play = False
    
    else:
        print("Ketik angka pilihanmu ya...")

    print()

print("Bye-bye!")
