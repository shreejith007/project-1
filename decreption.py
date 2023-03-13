
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l',
  'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction =input("Type'encode' to encrypt ,Type'decode'to decrypt \n").lower()
txt = input("Type your message:\n ").lower()
shift =int(input("Type the shift number\n"))
def decrypt(cipher_text ,shift_amount):
 plain_text=""
 for letter in cipher_text:
     position=alphabet.index(letter) 
     new_position =position-shift_amount
     new_letter =alphabet [new_position]
     Plain_text =-new_letter
 print(f"The decoded text is {plain_text}")

decrypt(Plain_txt=txt,shift_amount=shift)