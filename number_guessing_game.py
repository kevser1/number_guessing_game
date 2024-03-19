from random import randint

EASY_LEVEL_TURNS=10 #Kolay zorluk seviyesi için tahmin hakkı
HARD_LEVEL_TURNS=5 #Zor zorluk seviyesi için tahmin hakkı
"""iki sabit değişken tanımlıyoruz, bu değişkenler kullanıcının tahmin
hakkını belirlemek için kullanılacak"""

def check_answer(guess,answer, turns):
    """kullanıcının tahminini gerçek cevapla karşılaştırır ve
tahmin hakkını günceller"""
    if guess > answer:
        print("Too high.") #tahmin çok yüksekse kullanıcıya bilgi ver
        return turns -1 #kalan tahmin hakkını bir azalt ve döndür
    elif guess < answer:
        print("Too low.") #tahmin çok düşükse kullanıcıya bilgi ver
        return turns -1 #kalan tahmin hakkını bir azalt ve döndür
    else:
        print(f"You gor it! The answer was {answer}.")#tahmin doğruysa doğru cevabı ve bir tebrik mesajı göster
        return 0 #oyunun bitmesini sağlamak için 0 döndür

def set_difficulty():
    """Kullanıcıya oyunun zorluk seviyesini seçme seçeneği sunar."""
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level =="easy":
        return EASY_LEVEL_TURNS #Eğer easy seçeneği seçilirse, tahmin hakkı easy level turns olur
    else:
        return HARD_LEVEL_TURNS #hard seçeneği seçilirse, tahmin hakkı hard level turns olur
    
    
def game():
    """Oyunun ana mantığını içerir"""
    print("Welcome to the Number Guessing Game!") #oyun başladığında hoş geldin mesajı göster
    print("I'm thinking of a number between 1 and 100.")#kullanıcıya tahmin etmesi gereken sayı aralığını belirt
    answer=randint(1,100) #1 ile 100 arasında rastgele bir sayı seç ve bu sayıyı sakla
    print(f"Pssst, the correct answer is {answer}") #Doğru cevabı kullanıcıya göster (test amaçlı)
    
    turns=set_difficulty() #kullanıcıya oyunun zorluk seviyesini belirtmesini söyle ve tahmin hakkını ayarla
    
    while turns >0: #Kullanıcı tahmin hakkı kalmadığı sürece bir döngü başlat
        print("You've run out of guesses, you lose. ") #kullanıcıya bilgi ver ve oyunu kaybettiğini söyle
        
        guess=int(input("Make a guess:")) #kullanıcıdan bir tahmin yapmasını iste
        
        turns=check_answer(guess, answer,turns)# Kullanıcının tahminini kontrol et ve kalan tahmin hakkını güncelle
        if turns == 0:  # Eğer tahmin hakkı kalmadıysa
            print("You've run out of guesses, you lose.")  # Kullanıcıya bilgi ver ve oyunu kaybettiğini söyle
            return  # Oyundan çık
        elif guess != answer:  # Eğer tahmin yanlışsa
            print("Guess again.")  # Kullanıcıya bilgi ver ve tekrar tahmin yapmasını iste
            
game() #oyunu başlat


#100 Days of Code
