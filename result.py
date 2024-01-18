#Importē pandas bibliotēku un piešķir tai saīsinājumu "pd"
import pandas as pd

#Norāda Excel faila ceļu
file_path = "saraksts.xlsx"

#Nolasa DataFrame no Excel faila, norādot, ka tukšie lauki ir jāaizpilda ar tukšumu (na_values="")
df = pd.read_excel(file_path, na_values="", engine="openpyxl")

while True:
  print("1. Uzzināt lietotājvārdu/e-pastu un paroli!")
  print("2. Pievienot!")
  print("3. Izdzēst!")
  print("4. Beigt darbu!")

  choice = input("Kuru darbību vēlies veikt? (1/2/3/4): ")

  # 1. Uzzināt lietotājvārdu/e-pastu un paroli
  if choice == "1": 
    print("*" * 50)
    addrese = input("Ievadi adresi: ")
    info = df[df["Address"] == addrese]  #Filtrē DataFrame, atgriežot tikai rindas ar norādīto adresi
    if not info.empty: #Pārbauda, vai atbilstošais ieraksts eksistē
      print("Lietotājvārds/e-pasts:", info["Username"].values[0])
      print("Parole:", info["Password"].values[0])        
    else:
      print("Nav pievienots!")

  # 2. Pievienot jaunu ierakstu
  elif choice == "2":
    print("*" * 50)


  # 3. Izdzēst ierakstu pēc adreses
  elif choice == "3":
    print("*" * 50)
    addrese = input("Ievadi adresi, kuru vēlies izdzēst: ")
    df = df[df["Address"] != addrese] #Filtrē DataFrame, izņemot rindas ar norādīto adresi
    df.to_excel(file_path, index=False, engine="openpyxl")  #Saglabā DataFrame bez izdzēstajām rindām Excel failā, izmantojot openpyxl
    print("Informācija izdzēsta!")

  # 4. Beigt darbu un iziet no cikla
  elif choice == "4":
    break

  # Ja ievadītais neatbilst nevienai pieejamai iespējai
  else:
    print("Šādas izvēles nav!")
