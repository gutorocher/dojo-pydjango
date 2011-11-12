import unittest
import jogodavelha

class TestJogoDaVelha(unittest.TestCase):
  def test_chosen_position_is_valid(self):
      position_x = 1
      position_y = 2

      self.assertTrue(jogodavelha.is_position_valid(position_x, position_y))

  def test_select_position(self):
      position_x = 1
      position_y = 2 # [1,2]
      jogador = 1

      self.assertTrue(jogodavelha.select_position(position_x, position_y, jogador))