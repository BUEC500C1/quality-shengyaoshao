from ItoR import convert
def test():
  assert convert(10) == 'X'
  assert convert(25) == 'XXV'
  assert convert(55) == 'LV'
  assert convert(100) == 'C'
  assert convert(230) == 'CCXXX'
  assert convert(276) == 'CCLXXVI'  
  assert convert(365) == 'CCCLXV'  
  assert convert(962) == 'CMLXII'  
  assert convert(2365) == 'MMCCCLXV'  
  assert convert(-1) == 'Number must be an integer between 1 and 3999'  
  assert convert('AA') == 'The input must be an integer'  
