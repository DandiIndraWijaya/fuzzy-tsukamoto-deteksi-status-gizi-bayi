

# umur = int(input('Umur (bulan): '))
# berat_badan = float(input('Berat badan (kg): '))
# tinggi_badan = int(input('Tinggi badan (cm): '))

def deteksi_gizi_bayi_laki(umur, berat_badan, tinggi_badan):
  return deteksi(umur, berat_badan, tinggi_badan, gender="laki")

def deteksi_gizi_bayi_perempuan(umur, berat_badan, tinggi_badan):
  return deteksi(umur, berat_badan, tinggi_badan, gender="perempuan")

def fase_1(b,a,x):
    if(x<=a):
        nilai = 1
    elif(x>a and x<b):
        nilai = (b-x)/(b-a)
    elif(x>=b):
        nilai = 0

    return nilai

def fase_2(c,b,a,x):
  if(x==c):
    nilai = 1
  elif(x>a and x<c):
    nilai = (c-x)/(c-a)
  elif(x>c and x<b):
    nilai = (x-c)/(b-c)
  elif(x<=a or x>=b):
    nilai = 0
  
  return nilai

def fase_3(c,b,a,x):
  if(x==c):
    nilai = 1
  elif(x>a and x<c):
    nilai = (c-x)/(c-a)
  elif(x>c and x<b):
    nilai = (x-c)/(b-c)
  elif(x<=a or x>=b):
    nilai = 0
  
  return nilai

def fase_4(c,b,a,x):
  if(x==c):
    nilai = 1
  elif(x>a and x<c):
    nilai = (c-x)/(c-a)
  elif(x>c and x<b):
    nilai = (x-c)/(b-c)
  elif(x<=a or x>=b):
    nilai = 0
  
  return nilai

def fase_5(b,a,x):
    if(x<=a):
        nilai = 0
    elif(x>a and x<b):
        nilai = (x-a)/(b-a)
    elif(x>=b):
        nilai = 1

    return nilai

def turun(b,a,x):
    if(x<=a):
        nilai = 1
    elif(x>a and x<b):
        nilai = (b-x)/(b-a)
    elif(x>=b):
        nilai = 0

    return nilai

def sedang(c,b,a,x):
    if(x==c):
      nilai = 1
    elif(x>a and x<c):
      nilai = (c-x)/(c-a)
    elif(x>c and x<b):
      nilai = (x-c)/(b-c)
    elif(x<=a or x>=b):
      nilai = 0
    
    return nilai

def naik(b,a,x):
    if(x<=a):
        nilai = 0
    elif(x>a and x<b):
        nilai = (x-a)/(b-a)
    elif(x>=b):
        nilai = 1

    return nilai

def agregasi_gizi_buruk(b,a,alfa):
    nilai = b - (alfa*(b-a))
    return nilai

def agregasi_gizi_kurang(b,a,alfa):
  nilai = alfa*(b-a) + a
  return nilai

def agregasi_gizi_normal(b,a,alfa):
    nilai = alfa*(b-a) + a
    return nilai

def agregasi_gizi_lebih(b,a,alfa):
    nilai = alfa*(b-a) + a
    return nilai

def agregasi_obesitas(b,a,alfa):
    nilai = alfa*(b-a) + a
    return nilai


def deteksi(umur, berat_badan, tinggi_badan, gender):
  soal = dict()
  
  soal = {
      'umur': umur
  }
  soal_2 = {
      'berat_badan': berat_badan,
      'tinggi_badan': tinggi_badan
  }
  nama_var = ['umur', 'berat_badan', 'tinggi_badan', 'gizi']
  variabel = dict()
  
  if gender == 'laki':
    variabel = {
      'fase_1': 6,
      'fase_2': 12,
      'fase_3': 24,
      'fase_4': 36,
      'fase_5': 46, 
      'berat_badan_down': 7,
      'berat_badan_sedang': 13,
      'berat_badan_up': 19,
      'tinggi_badan_down': 49,
      'tinggi_badan_sedang': 75,
      'tinggi_badan_up': 101
    }
    
  else:
    variabel = {
      'fase_1': 6,
      'fase_2': 12,
      'fase_3': 24,
      'fase_4': 36,
      'fase_5': 46, 
      'berat_badan_down': 7,
      'berat_badan_sedang': 12,
      'berat_badan_up': 18,
      'tinggi_badan_down': 48,
      'tinggi_badan_sedang': 74,
      'tinggi_badan_up': 100
  }
    
  nk_1 = dict()
  nk = dict()
  nk_fase_1 = fase_1(variabel['fase_1'], variabel['fase_2'], soal['umur'])
  nk_fase_2 = fase_2(variabel['fase_2'], variabel['fase_3'], variabel['fase_1'], soal['umur'])
  nk_fase_3 = fase_3(variabel['fase_3'], variabel['fase_4'], variabel['fase_2'], soal['umur'])
  nk_fase_4 = fase_4(variabel['fase_4'], variabel['fase_5'], variabel['fase_3'], soal['umur'])
  nk_fase_5 = fase_5(variabel['fase_5'], variabel['fase_4'], soal['umur'])

  nk_1.update({'fase_1': nk_fase_1})
  nk_1.update({'fase_2': nk_fase_2})
  nk_1.update({'fase_3': nk_fase_3})
  nk_1.update({'fase_4': nk_fase_4})
  nk_1.update({'fase_5': nk_fase_5})

  for i in soal_2:
      up = naik(variabel[i+"_up"],variabel[i+"_down"],soal_2[i])
      rata = sedang(variabel[i+"_sedang"],variabel[i+"_up"],variabel[i+"_down"],soal_2[i])
      down = turun(variabel[i+"_up"],variabel[i+"_down"],soal_2[i])
      nk.update({i+"_up":up})
      nk.update({i+"_sedang": rata})
      nk.update({i+"_down":down})


  #AGREGASI
  alfa = []
  z = []

  rules = [
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_1',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'obesitas'
          },
          {
              #10
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_2',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'obesitas'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'buruk'
          },
          {
              #20
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'buruk'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'buruk'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_3',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'obesitas'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'kurang'
          },
          {
              #30
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'sedang'
          },
          {
            'fase': 'fase_4',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'normal'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'buruk'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'buruk'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_down',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'buruk'
          },
          {
              #40
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_sedang',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'kurang'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_down',
            'kesimpulan': 'lebih'
          },
          {
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_sedang',
            'kesimpulan': 'lebih'
          },
          {
              #45
            'fase': 'fase_5',
            'berat_badan': 'berat_badan_up',
            'tinggi_badan': 'tinggi_badan_up',
            'kesimpulan': 'normal'
          },
  ]


  for i in rules:
    a = min(nk_1[i['fase']], nk[i['berat_badan']], nk[i['tinggi_badan']])
    alfa.append(a)
    if(i['kesimpulan'] == 'buruk'):
      zz = agregasi_gizi_buruk(48, 43, a)
    elif(i['kesimpulan'] == 'kurang'):
      zz = agregasi_gizi_kurang(48, 43, a)
    elif(i['kesimpulan'] == 'normal'):
      zz = agregasi_gizi_normal(53, 48, a)
    elif(i['kesimpulan'] == 'lebih'):
      zz = agregasi_gizi_lebih(70, 53, a)
    elif(i['kesimpulan'] == 'obesitas'):
      zz = agregasi_gizi_lebih(83, 70, a)
    z.append(zz)


  # print(alfa)
  # print(z)

  #DEFUZIFIKASI
  df = 0

  for i in range(len(alfa)):
      df += alfa[i]*z[i]

  defuz = round(df/sum(alfa), 2)
  dit = 'Variabel yang ditanyakan : gizi'
  
  if defuz < 43:
    status = 'Gizi Buruk'
  
  elif defuz > 43 and defuz < 48:
    status = 'Gizi Kurang'
  
  elif defuz > 48 and defuz < 70:
    status = 'Normal'
  
  elif defuz > 70 and defuz < 83:
    status = 'Gizi Lebih'
    
  elif defuz > 83:
    status = 'Obesitas'
    
  # print("Jadi, nilai ",dit," adalah ",defuz)
  return [status, defuz]


# deteksi_gizi_bayi_laki(15, 18, 25)