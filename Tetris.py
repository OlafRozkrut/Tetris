import pygame
import random

pygame.init()

size = width, height = 900, 750
screen = pygame.display.set_mode(size)

run = True

# Kolory
GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)               # 1 't'
GREEN = (0, 255, 0)             # 2 'o'
LIGHT_BLUE = (135, 206, 250)   # 3 'i'
PINK = (255, 105, 180)         # 4 's'
ORANGE = (255, 140, 0)         # 5 'z'
YELLOW = (255, 255, 0)            # 6 'j'
DARK_BLUE = (0, 0, 205)         # 7 'l'
PURPLE = (186, 85, 211)

# Klasa Figura
class Figura:
    pola_f = []
    najnizsze_pole = None
    
    def __init__(self):
        self.nastepny = self.wylosuj_figure()
        self.jaki = self.wylosuj_figure()
        self.stworz_nowy(self.jaki)
        self.ile_razy_obrocony = 0
        self.trzymany = ''
        self.mega_szybko = 0
        self.stan = 1
    
    def okreslenie_najnizszego(self):
        self.najnizsze_pole = self.pola_f[0][1]
        for i in range(1, 4):
            if self.pola_f[i][1] < self.najnizsze_pole:
                self.najnizsze_pole = self.pola_f[i][1]

    def rotacja(self):
        if self.jaki == 'o':
            return
        elif self.jaki == 't': #srodkowy [0]
            #stan 1 - nie ma gornego
            #stan 2 - nie ma prawego
            #stan 3 - nie ma dolnego
            #stan 4 - nie ma lewego
            if self.stan == 1:#usuwamy wszystkie oprocz srodkowego 
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.stan += 1
            elif self.stan == 2:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.stan += 1
            elif self.stan == 3:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.stan += 1
            elif self.stan == 4:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.stan = 1
        elif self.jaki == 'l':
            if self.stan == 1:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]-1])#dodanie gorna-lewo
                self.stan += 1
            elif self.stan == 2:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]-1])#dodanie gora-prawo
                self.stan += 1
            elif self.stan == 3:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]+1])#dodanie dol-prawo
                self.stan += 1
            elif self.stan == 4:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]+1])#dodanie dol-lewo
                self.stan = 1
        elif self.jaki == 'j':
            if self.stan == 1:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]+1])#dodanie dol-lewo
                self.stan += 1
            elif self.stan == 2:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]-1])#dodanie gorna-lewo
                self.stan += 1
            elif self.stan == 3:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]-1])#dodanie gora-prawo
                self.stan += 1
            elif self.stan == 4:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]+1])#dodanie dol-prawo
                self.stan = 1
        elif self.jaki == 'z':
            if self.stan == 1:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]-1])#dodanie gora-prawo
                self.stan += 1
            elif self.stan == 2:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]+1])#dodanie dol-prawo
                self.stan = 1
        elif self.jaki == 's':
            if self.stan == 1:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]+1])#dodanie dol-prawo
                self.stan += 1
            elif self.stan == 2:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]+1])#dodanie dol-lewo
                self.stan = 1
        elif self.jaki == 'i':
            if self.stan == 1:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]-1])#dodanie gornego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+1])#dodanie dolnego
                self.pola_f.append([self.pola_f[0][0],self.pola_f[0][1]+2])#dodanie 2-dolny
                self.stan += 1
            elif self.stan == 2:
                del self.pola_f[3]
                del self.pola_f[2]
                del self.pola_f[1]
                self.pola_f.append([self.pola_f[0][0]-1,self.pola_f[0][1]])#dodanie lewego
                self.pola_f.append([self.pola_f[0][0]+1,self.pola_f[0][1]])#dodanie prawego
                self.pola_f.append([self.pola_f[0][0]-2,self.pola_f[0][1]])#dodanie 2-lewego
                self.stan = 1

    def grawitacja(self, plansza, current_time, czas_spadania):
        # Sprawdzamy, czy upłynął czas dla grawitacji
        if current_time - self.last_gravity_time > czas_spadania:
            self.okreslenie_najnizszego()
            czy_spada = True
            for i in range(4):
                # Sprawdzamy, czy klocek dotyka ziemi lub innego klocka
                if (self.pola_f[i][1] + 1) > 19 or plansza.pola[self.pola_f[i][1] + 1][self.pola_f[i][0]] > 0:
                    czy_spada = False

            if czy_spada:
                for i in range(4):
                    self.pola_f[i][1] += 1  # Zwiększ współrzędną Y o 1, aby klocek spadł
            else:
                self.zmiana_na_stale(plansza)
                self.stworz_nowy(self.nastepny)
                self.jaki = self.nastepny
                self.nastepny = self.wylosuj_figure()
                self.ile_razy_obrocony = 0
                self.mega_szybko = 0
                

            plansza.czyszczenie()  # Czyszczenie planszy przed rysowaniem
            self.wstawienie_figury(plansza)
            self.last_gravity_time = current_time  # Ustawiamy ostatni czas spadania

    def wstawienie_figury(self, plansza):
        for i in range(4):
            plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = -1  # Ustawienie klocka na planszy

    def zmiana_na_stale(self, plansza):
        if self.jaki == 't':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 1
        elif self.jaki == 'o':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 2
        elif self.jaki == 'i':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 3
        elif self.jaki == 's':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 4
        elif self.jaki == 'z':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 5
        elif self.jaki == 'j':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 6
        elif self.jaki == 'l':
            for i in range(4):
                plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]] = 7

    def stworz_nowy(self,jaki):
        self.pola_f.clear()
        self.stan = 1
        if jaki == 'i':
            self.pola_f.append([4, 0])
            self.pola_f.append([5, 0])
            self.pola_f.append([6, 0])
            self.pola_f.append([3, 0])
        elif jaki == 't':
            self.pola_f.append([5, 0])
            self.pola_f.append([4, 0])
            self.pola_f.append([6, 0])
            self.pola_f.append([5, 1])
        elif jaki == 'o':
            self.pola_f.append([5, 0])
            self.pola_f.append([5, 1])
            self.pola_f.append([4, 0])
            self.pola_f.append([4, 1])
        elif jaki == 'l':
            self.pola_f.append([5, 0])
            self.pola_f.append([4, 0])
            self.pola_f.append([6, 0])
            self.pola_f.append([4, 1])
        elif jaki == 'j':
            self.pola_f.append([5, 0])
            self.pola_f.append([4, 0])
            self.pola_f.append([6, 0])
            self.pola_f.append([6, 1])
        elif jaki == 's':
            self.pola_f.append([4, 1])
            self.pola_f.append([5, 1])
            self.pola_f.append([5, 0])
            self.pola_f.append([6, 0])
        elif jaki == 'z':
            self.pola_f.append([4, 0])
            self.pola_f.append([5, 0])
            self.pola_f.append([5, 1])
            self.pola_f.append([6, 1])

    def przesuniecie_lewo(self,plansza):
        for i in range(4):
            if self.pola_f[i][0] == 0 or moja_plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]-1] > 0:
                return
        for i in range(4):
            self.pola_f[i][0] -= 1  # Zmniejsz współrzędną X

    def przesuniecie_prawo(self,plansza):
        for i in range(4):
            if  self.pola_f[i][0] == 9 or moja_plansza.pola[self.pola_f[i][1]][self.pola_f[i][0]+1] > 0:
                return
        for i in range(4):
            self.pola_f[i][0] += 1  # Zwiększ współrzędną X

    def hold(self):
        if self.trzymany == '':
            self.stworz_nowy(self.nastepny)
            self.trzymany = self.jaki
            self.jaki = self.nastepny
            self.nastepny = self.wylosuj_figure()
        else:
            temp = self.trzymany
            self.trzymany = self.jaki
            self.jaki = temp
            self.stworz_nowy(self.jaki)
    

    def wylosuj_figure(self):
        n = random.randint(1, 7)
        if n == 1:
            return 'i'
        elif n == 2:
            return 't'
        elif n == 3:
            return 'o'
        elif n == 4:
            return 'l'
        elif n == 5:
            return 'j'
        elif n == 6:
            return 's'
        elif n == 7:
            return 'z'


# Klasa Plansza
class Plansza:
    def __init__(self):
        self.pola = [[0] * 10 for _ in range(20)]  # 0-puste pole, 1- solidny blok, -1- spadający blok
        self.ile_wyczyszczonych_linii = 0
        self.level = 1
        self.score = 0
        self.ile_wyczyszczonych_w_ciagu_sekundy = 0
    
    def pokaz_plansze(self):
        for row in self.pola:
            print(row)

    def czyszczenie(self):
        for i in range(len(self.pola)):
            for j in range(len(self.pola[i])):
                if self.pola[i][j] == -1:  # Spadające bloki zostają wyczyszczone
                    self.pola[i][j] = 0

    def pelen_wiersz(self):
        for i in range(len(self.pola)):
            suma = 0
            for j in range(len(self.pola[i])):
                if self.pola[i][j] > 0:
                    suma += 1
            if suma == 10:
                del self.pola[i]
                self.pola.insert(0,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                self.ile_wyczyszczonych_linii += 1
                self.ile_wyczyszczonych_w_ciagu_sekundy += 1
    def akutalizuj_level(self):
        self.level = 1 + self.ile_wyczyszczonych_linii//4
    def add_score(self):
        ile_lini = self.ile_wyczyszczonych_w_ciagu_sekundy
        if ile_lini == 1:
            self.score += 40*self.level
        elif ile_lini == 2:
            self.score += 100*self.level
        elif ile_lini == 3:
            self.score += 300*self.level
        elif ile_lini == 4:
            self.score += 1200*self.level
        


moja_plansza = Plansza()


x, y = 300, 50
side_length = 30
obramowka = 2
klocek = Figura() 
klocek.wstawienie_figury(moja_plansza)

def rysuj_plansze():
    num_rows = len(moja_plansza.pola)
    num_cols = len(moja_plansza.pola[0])
    
    # Rozmiar czarnego kwadratu (całkowicie pokrywającego kratki obramówki)
    square_size = side_length - obramowka / 2

    # Rysowanie czarnych kwadratów na obramówce (góra i dół)
    for col in range(-1, num_cols + 1):
        # Górna obramówka
        black_x = x + side_length * col - obramowka * col
        black_y = y - side_length + obramowka # Pozycja powyżej planszy
        pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
        
        # Dolna obramówka
        black_y = y + side_length * num_rows - obramowka * num_rows
        pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
    
    # Rysowanie czarnych kwadratów na obramówce (lewa i prawa)
    for row in range(num_rows):
        # Lewa obramówka
        black_x = x - side_length + obramowka  # Pozycja po lewej stronie planszy
        black_y = y + side_length * row - obramowka * row
        pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
        
        # Prawa obramówka
        black_x = x + side_length * num_cols - obramowka * num_cols
        pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))

    # Rysowanie wnętrza planszy
    for i in range(num_rows):
        for j in range(num_cols):
            black_x = x + side_length * j - obramowka * j  # Pozycja w poziomie
            black_y = y + side_length * i - obramowka * i  # Pozycja w pionie
            if moja_plansza.pola[i][j] == 0:
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, GRAY, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 1 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 't'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, RED, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 2 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 'o'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, GREEN, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 3 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 'i'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, LIGHT_BLUE, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 4 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 's'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, PINK, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 5 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 'z'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, ORANGE, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 6 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 'j'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, YELLOW, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))
            elif moja_plansza.pola[i][j] == 7 or (moja_plansza.pola[i][j] == -1 and klocek.jaki == 'l'):
                pygame.draw.rect(screen, BLACK, (black_x, black_y, square_size, square_size))
                pygame.draw.rect(screen, DARK_BLUE, (black_x + obramowka / 2, black_y + obramowka / 2, side_length - obramowka - obramowka / 2, side_length - obramowka - obramowka / 2))


clock = pygame.time.Clock()

speed = 300#fps
ruch_interval = 200  # Interwał dla ruchu lewo/prawo
ostatni_ruch = pygame.time.get_ticks()  # Czas w milisekundach od rozpoczęcia gry
czas_spadania = 300  # Czas w milisekundach pomiędzy spadaniami klocków
klocek.last_gravity_time = pygame.time.get_ticks()  # Czas ostatniego spadania
normalny_czas = czas_spadania
font = pygame.font.Font(None, 74)  # None oznacza domyślną czcionkę systemową, 74 to rozmiar
font2 = pygame.font.Font(None, 30)
text_next = font.render("NEXT:", True, BLACK)  
text_rect_next = text_next.get_rect(center=(750, 100))
text_hold = font.render("HOLD:", True, BLACK) 
text_rect_hold = text_hold.get_rect(center=(120, 100))
text_instrukcje = font2.render("Prawo: <-   Lewo: ->    Hold: c     Rotacja: z", True, BLACK) 
text_rect_instrukcje = text_hold.get_rect(center=(300, 700))
text_instrukcje2 = font2.render("Szybko w dol: dolna strzalka        Od razu w dol: spacja", True, BLACK)  
text_rect_instrukcje2 = text_hold.get_rect(center=(250, 730))
text_score = font.render("SCORE:", True, BLACK)  
text_rect_score = text_next.get_rect(center=(750, 400))
text_level = font.render("LEVEL:", True, BLACK)  
text_rect_level = text_next.get_rect(center=(700, 600))

ostatni_level = 1
time_elapsed = 0
while run:
    screen.fill(PURPLE)

    current_time = pygame.time.get_ticks()
    dt = clock.tick(300)  # Ograniczenie do 60 klatek na sekundę
    time_elapsed += dt

    klocek.grawitacja(moja_plansza, current_time, czas_spadania)  # Sprawdzamy i wykonujemy grawitację dla klocka
    moja_plansza.pelen_wiersz()
    rysuj_plansze()  # Rysujemy planszę
    # Sprawdzanie stanu klawiszy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and current_time - ostatni_ruch > ruch_interval:  # Klawisz D przesuwa w prawo
        klocek.przesuniecie_prawo(moja_plansza)
        ostatni_ruch = current_time
    if keys[pygame.K_LEFT] and current_time - ostatni_ruch > ruch_interval:  # Klawisz A przesuwa w lewo
        klocek.przesuniecie_lewo(moja_plansza)
        ostatni_ruch = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:  # Sprawdzamy, czy naciśnięto przycisk
                czas_spadania /= 6
                normalny_czas /= 6  # Aktywujemy ruch, bo klawisz jest trzymany
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:  # Sprawdzamy, czy zwolniono przycisk
                czas_spadania *= 6
                normalny_czas *= 6

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Sprawdzamy, czy naciśnięto przycisk
                klocek.hold()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:  # Sprawdzamy, czy naciśnięto przycisk
                klocek.rotacja()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Sprawdzamy, czy naciśnięto przycisk
                normalny_czas = czas_spadania
                klocek.mega_szybko = 1
                czas_spadania = 0
    if klocek.mega_szybko == 0:
        czas_spadania = normalny_czas
    if time_elapsed >= 1000:  # 1000 ms = 1 sekunda
        moja_plansza.add_score()
        time_elapsed = 0
        moja_plansza.ile_wyczyszczonych_w_ciagu_sekundy = 0 
    moja_plansza.akutalizuj_level()
    if moja_plansza.level > ostatni_level:
        czas_spadania = max(50, int(czas_spadania * 0.5))  # Zapewnia minimalne tempo
        ostatni_level = moja_plansza.level
    clock.tick(speed)
    if klocek.nastepny == 'o':
        pygame.draw.rect(screen, GREEN, (690, 150, 30, 30))
        pygame.draw.rect(screen, GREEN, (720, 150, 30, 30))
        pygame.draw.rect(screen, GREEN, (690, 180, 30, 30))
        pygame.draw.rect(screen, GREEN, (720, 180, 30, 30))
    elif klocek.nastepny == 't':
        pygame.draw.rect(screen, RED, (690, 150, 30, 30))
        pygame.draw.rect(screen, RED, (720, 150, 30, 30))
        pygame.draw.rect(screen, RED, (750, 150, 30, 30))
        pygame.draw.rect(screen, RED, (720, 180, 30, 30))
    elif klocek.nastepny == 'i':
        pygame.draw.rect(screen, LIGHT_BLUE, (690, 150, 30, 30))
        pygame.draw.rect(screen, LIGHT_BLUE, (720, 150, 30, 30))
        pygame.draw.rect(screen, LIGHT_BLUE, (750, 150, 30, 30))
        pygame.draw.rect(screen, LIGHT_BLUE, (780, 150, 30, 30))
    elif klocek.nastepny == 'l':
        pygame.draw.rect(screen, DARK_BLUE, (690, 150, 30, 30))
        pygame.draw.rect(screen, DARK_BLUE, (720, 150, 30, 30))
        pygame.draw.rect(screen, DARK_BLUE, (750, 150, 30, 30))
        pygame.draw.rect(screen, DARK_BLUE, (690, 180, 30, 30))
    elif klocek.nastepny == 'j':
        pygame.draw.rect(screen, YELLOW, (690, 150, 30, 30))
        pygame.draw.rect(screen, YELLOW, (720, 150, 30, 30))
        pygame.draw.rect(screen, YELLOW, (750, 150, 30, 30))
        pygame.draw.rect(screen, YELLOW, (750, 180, 30, 30))
    elif klocek.nastepny == 's':
        pygame.draw.rect(screen, PINK, (690, 180, 30, 30))
        pygame.draw.rect(screen, PINK, (720, 180, 30, 30))
        pygame.draw.rect(screen, PINK, (720, 150, 30, 30))
        pygame.draw.rect(screen, PINK, (750, 150, 30, 30))
    elif klocek.nastepny == 'z':
        pygame.draw.rect(screen, ORANGE, (690, 150, 30, 30))
        pygame.draw.rect(screen, ORANGE, (720, 150, 30, 30))
        pygame.draw.rect(screen, ORANGE, (720, 180, 30, 30))
        pygame.draw.rect(screen, ORANGE, (750, 180, 30, 30))
    
    
    if klocek.trzymany == 'o':
        pygame.draw.rect(screen, GREEN, (90, 150, 30, 30))
        pygame.draw.rect(screen, GREEN, (120, 150, 30, 30))
        pygame.draw.rect(screen, GREEN, (90, 180, 30, 30))
        pygame.draw.rect(screen, GREEN, (120, 180, 30, 30))
    elif klocek.trzymany == 't':
        pygame.draw.rect(screen, RED, (90, 150, 30, 30))
        pygame.draw.rect(screen, RED, (120, 150, 30, 30))
        pygame.draw.rect(screen, RED, (150, 150, 30, 30))
        pygame.draw.rect(screen, RED, (120, 180, 30, 30))
    elif klocek.trzymany == 'i':
        pygame.draw.rect(screen, LIGHT_BLUE, (90, 150, 30, 30))
        pygame.draw.rect(screen, LIGHT_BLUE, (120, 150, 30, 30))
        pygame.draw.rect(screen, LIGHT_BLUE, (150, 150, 30, 30))
        pygame.draw.rect(screen, LIGHT_BLUE, (180, 150, 30, 30))
    elif klocek.trzymany == 'l':
        pygame.draw.rect(screen, DARK_BLUE, (90, 150, 30, 30))
        pygame.draw.rect(screen, DARK_BLUE, (120, 150, 30, 30))
        pygame.draw.rect(screen, DARK_BLUE, (150, 150, 30, 30))
        pygame.draw.rect(screen, DARK_BLUE, (90, 180, 30, 30))
    elif klocek.trzymany == 'j':
        pygame.draw.rect(screen, YELLOW, (90, 150, 30, 30))
        pygame.draw.rect(screen, YELLOW, (120, 150, 30, 30))
        pygame.draw.rect(screen, YELLOW, (150, 150, 30, 30))
        pygame.draw.rect(screen, YELLOW, (150, 180, 30, 30))
    elif klocek.trzymany == 's':
        pygame.draw.rect(screen, PINK, (90, 180, 30, 30))
        pygame.draw.rect(screen, PINK, (120, 180, 30, 30))
        pygame.draw.rect(screen, PINK, (120, 150, 30, 30))
        pygame.draw.rect(screen, PINK, (150, 150, 30, 30))
    elif klocek.trzymany == 'z':
        pygame.draw.rect(screen, ORANGE, (90, 150, 30, 30))
        pygame.draw.rect(screen, ORANGE, (120, 150, 30, 30))
        pygame.draw.rect(screen, ORANGE, (120, 180, 30, 30))
        pygame.draw.rect(screen, ORANGE, (150, 180, 30, 30))
    text_score2 = font.render(str(moja_plansza.score), True, BLACK)  # True oznacza antyaliasing (wygładzanie tekstu)
    text_rect_score2 = text_next.get_rect(center=(800, 450))
    text_level2 = font.render(str(moja_plansza.level), True, BLACK)  # True oznacza antyaliasing (wygładzanie tekstu)
    text_rect_level2 = text_next.get_rect(center=(900, 600))
    screen.blit(text_next, text_rect_next)
    screen.blit(text_hold, text_rect_hold)
    screen.blit(text_instrukcje, text_rect_instrukcje)
    screen.blit(text_instrukcje2, text_rect_instrukcje2)
    screen.blit(text_score, text_rect_score)
    screen.blit(text_score2, text_rect_score2)
    screen.blit(text_level, text_rect_level)
    screen.blit(text_level2, text_rect_level2)
    pygame.display.update()
    for i in range(10):
        if moja_plansza.pola[0][i] > 0:
            run = False

pygame.quit()
