print("Welcome to the Govt. Mental Health Service Assistance Machine")

healing_quotes = {
    '1': "Tears are words the heart can’t express. Let them flow, and know that brighter days are ahead.",
    '2': "Breathe in deeply, and remind yourself that you are safe. This moment will pass.",
    '3': "You may feel alone, but you’re surrounded by a world that cares. Reach out, and you’ll find connection.",
    '4': "Frustration is the first step towards improvement. Release what you can’t control, and keep moving forward.",
    '5': "Take a deep breath. Anger is like a fire; you can let it burn, or you can let it warm your heart and guide you.",
    '6': "Courage doesn’t mean you’re not afraid. It means facing fear with a brave heart.",
    '7': "Believe in yourself, and the world will believe in you too. You have all the power you need within.",
    '8': "In confusion, we find new paths. Embrace the journey and trust yourself.",
    '9': "Remember, your journey is uniquely yours. Celebrate others’ wins, and focus on your own growth.",
    '10': "It’s okay to rest. You don’t have to be strong all the time."
}


user_input = input(
         "\nWhat's your feeling right now?\n"
         "1) Sad\n"
         "2) Anxiety\n"
         "3) Lonely\n"
         "4) Frustration\n"
         "5) Anger\n"
         "6) Fear\n"
         "7) Self-doubt\n"
         "8) Confusion\n"
         "9) Jealousy\n"
         "10) Tiredness\n"
     )

if user_input in healing_quotes:
    print("\nHealing Quote for You:")
    print(healing_quotes[user_input])
else:
    print("Invalid entry. Please enter a number from 1 to 10")
    
# planning to collect more details from user and integrating with chatgpt to provide result
