név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ')

kor = int(kor)
év = input('melyik évben járunk? ')
év = int(év)

születési_év = év - kor
print(név, ', kend ', születésiév, '-ban született.', sep='')