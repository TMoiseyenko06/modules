def mood_response(mood):
    bad_moods = ['sad','angry']
    good_moods = ['happy','excited']
    if mood in good_moods:
        return 'Im glad to hear that!'
    elif mood in bad_moods:
        return 'I hope you get better!'
    else:
        return 'I feel the same way!'