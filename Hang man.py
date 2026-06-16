import random


player_hp = 6

word_gen = {
    "Monika": ["m", "o", "n", "i", "k", "a"],
    "Hadai": ["h", "a", "d", "a", "i"],
    "Aubrey": ["a", "u", "b", "r", "e", "y"],
    "Joey": ["j", "o", "e", "y"],
    "Lilly": ["l", "i", "l", "l", "y"],
    "Ashly": ["a", "s", "h", "l", "y"],
    "Pocky": ["p", "o", "c", "k", "y"],
    "Basil": ["b", "a", "s", "i", "l"],
    "Sogeki": ["s", "o", "g", "e","k","i"],
    "komi": ["k", "o", "m", "i"],
    "sena": ["s", "e", "n", "a"]

}
random_sel_name = random.choice(list(word_gen.keys())).lower()
num_correct = 0
already_guessed = []
player_word = ["_"] * len(random_sel_name)
print(("".join(player_word).capitalize()))
while player_hp > 0:
    guess_word = input("Guess letter: ").lower()
    while guess_word in already_guessed:
        guess_word = input("You already guessed that letter. Try again: ").lower()
    already_guessed.append(guess_word)
    # Check if the guess is actually in the word AT ALL
    if guess_word in random_sel_name:
        print("Correct!")
        # Use your enumerate logic to update the player_word
        for i, letter in enumerate(random_sel_name):
            if letter == guess_word:
                player_word[i] = guess_word
    else:
        print("Incorrect")
        player_hp -= 1
    print(f"Word: "+ ("".join(player_word).capitalize())+".")
    print(f"HP: {player_hp}")
    print(f"Words already guessed: {already_guessed}")

    # Check for win condition
    if "_" not in player_word:
        print("You won!")
        print("The word was:" + ("".join(player_word).capitalize()))
        break

if player_hp <= 0:
    print("you die")
    print(random_sel_name.capatilized())






##random_sel_name = random.choice(list(word_gen.keys()))
##word_to_guess = random_sel_name
##word_to_guess = [word_to_guess]
