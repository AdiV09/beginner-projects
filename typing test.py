import time

print("Type the pop-up sentence as fast as you can after 3 seconds.")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
sentence = "Barily had a little lamb."

while True:
    t0 = time.time()
    input_text = input("Enter the sentence: " + sentence + "\n")
    t1 = time.time()
    if input_text != sentence:
        print("Whoops! You didn't type the sentence correctly!")
        quit()
    break

print("You took approximately " + str(round(t1 - t0)) + " seconds to type the sentence!")
