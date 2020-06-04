### Stuck saya bingung harus di buat gimana mas tadinya saya mau di pisah dulu 1 1 terus nanti di join lagi mas, 
# tapi saya bingung cara ngebuat huruf yg di ulang caranya

kalimat = input("masukan kalimat: ")
kalimat = kalimat.split(' ')
num = False
low = False
upp = False
result = []

for i in kalimat:
  kalimat_baru = ''
  if not kalimat.isupper() and not kalimat.islower():
    if kalimat[0].isnumeric():
        num = True
        low = False
        upp = False
    elif kalimat[0].islower():
        num = False
        low = True
        upp = False
    elif kalimat[0].isupper():
        num = False
        low = False
        upp = True
    for huruf in kalimat:
      if huruf.isnumeric():
        if num:
            kalimat_baru += huruf
        else:
            kalimat_baru += ' ' + huruf
        low = False
        upp = False
        num = True
      elif huruf.islower():
        if low or upp:
            kalimat_baru += huruf
        else:
            kalimat_baru += ' ' + huruf
        low = True
        upp = False
        num = False
      elif huruf.isupper():
        if low or num:
            kalimat_baru += ' ' + huruf
        else:
            kalimat_baru += huruf
        low = False
        upp = True
        num = False
      else:
        kalimat_baru += ' ' + kalimat
    result.append(''.join(kalimat_baru))
  else:
    result.append(kalimat)
' '.join(result)