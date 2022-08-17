from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
       if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
       if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_massage = ''.join(letter_list)
    return new_massage

def get_task():
    task = simpledialog.askstring('Görev','"Şifrele"mek mi yoksa "Şifresini\
 Çözmek" mi istiyorsunuz?')
    return task

def get_message():
    message = simpledialog.askstring('Mesaj','Gizli mesajı girin: ')
    return message

root: Tk()
while True:
    task = get_task()

    if task == 'Şifrele':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Gizli mesajın şifreli metni:', encrypted)

    elif task == 'Şifresini Çözmek':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Gizli mesajın açık metni:', decrypted)

    else:
        break
root.mainloop()

