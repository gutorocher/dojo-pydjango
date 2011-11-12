#coding: utf-8
def __init__(self):
   for i in range(0,2):
       for j in range(0,2):
           self.matriz[i][j] = 0

def select_position(self, position_x, position_y, jogador):
  if self.is_position_valid(position_x):
      raise Exception(u"Valor invalido para X")

  if self.is_position_valid(position_y):
      raise Exception(u"Valor invalido para Y")

  self.matriz[position_x][position_y] = jogador
  winner = self.check_winner()

  if winner is not None:
      print u"O vencedor eh", winner

def is_position_valid(self, position_x, position_y):
    if position_x > 2 or position_x < 0:
        return False
    if position_y > 2 or position_y < 0:
        return False
    if self.matriz[position_x][position_y] is not False:
        return False
    return True

def check_winner(self):
    for i in range(1,3):
        if (self.matriz[0][0] == i and self.matriz[0][1] == i and self.matriz[0][2] == i)  or (self.matriz[1][0] == i and self.matriz[1][1] == i and self.matriz[1][2] == i) or (self.matriz[2][0] == i and self.matriz[2][1] == i and self.matriz[2][2] == i) or (self.matriz[0][0] == i and self.matriz[1][0] == i and self.matriz[2][0] == i) or (self.matriz[0][1] == i and self.matriz[1][1] == i and self.matriz[2][1] == i) or (self.matriz[0][2] == i and self.matriz[1][2] == i and self.matriz[2][2] == i) or (self.matriz[0][0] == i and self.matriz[1][1] == i and self.matriz[2][2] == i) or (self.matriz[2][0] == i and self.matriz[1][1] == i and self.matriz[0][2] == i):
            return i
        elif i == 2:
            return None