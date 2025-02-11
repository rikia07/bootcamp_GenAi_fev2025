# cat's and dog's years
# écrire programme avec age humain-age chat-age chien
#list  [humanyears, catyears, dogyears]
def calculated_pet_years(humanyears):
 if humanyears ==1:
  return [humanyears, 15,15]
 elif humanyears==2:
  return [humanyears, 24, 24]
 else :
  cat_years = 24 + (humanyears-2)*4
  dog_years = 24  + (humanyears - 2)*4
  return [humanyears,cat_years, dog_years]
print(calculated_pet_years(1)) 
#  [1, 15, 15]
print(calculated_pet_years(2))
#  [2, 24, 24]
print(calculated_pet_years(10))
#   [10, 56, 64]  