i = 1
underweight = 0
normalweight = 0
overweight = 0
overages = float()
normalages = float()
underages = float()

while i < 3:
  height=float(input("Enter your height: "))
  weight=float(input("Enter your weight: "))
  age=float(input("Enter your age: "))

  #BMI calculation // BR: IMC
  height = height * height
  imc = weight/height

  #Assessments
  if imc < 20:
      underweight += 1
      underages += age
    
  if imc >= 20 and imc <= 25:
      normalweight += 1
      normalages += age
    
  if imc > 25:
      overweight += 11
      overages += age
    
  print("-=-" *15)
  r = int(input("Are there more participants? 1 = YES 0 = NO : "))
  if r != 1:
    break
  else:
    print("-=-" *15, "\n")

#Averages // Medias
if underweight > 1:
  underages /= underweight

if normalweight > 1:
  normalages /= normalweight

if overweight > 1:
  overages /= overweight

print("-=-" *15)
print("\nUnderweight participants: {}, average age: {:.2f}\n" .format(underweight, underages))
print("-=-" *15)
print("\nNormal weight participants: {}, average age: {:.2f}\n" .format(normalweight, normalages))
print("-=-" *15)
print("\nOverweight or obese participants {}, mean age: {:.2f}\n" .format(overweight, overages))
print("-=-" *15)
