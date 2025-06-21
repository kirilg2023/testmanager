from django.shortcuts import render

# Create your views here.
def main(request,main):
    if main == 'main':
        return render(request, 'quiz/main.html')
    if main == 'info':
        return render(request, 'quiz/info.html')
    if main == 'win':
        return render(request, 'quiz/win_lose/win.html')
    if main == 'lose':
        return render(request, 'quiz/win_lose/lose.html')

def game(request, q):
    if q == 'quest_1':
        return render(request, 'quiz/game/q1.html')
    if q == 'quest_2':
        return render(request, 'quiz/game/q2.html')
    if q == 'quest_3':
        return render(request, 'quiz/game/q3.html')
    if q == 'quest_4':
        return render(request, 'quiz/game/q4.html')
    if q == 'quest_5':
        return render(request, 'quiz/game/q5.html')
    if q == 'quest_6':
        return render(request, 'quiz/game/q6.html')
    if q == 'quest_7':
        return render(request, 'quiz/game/q7.html')
    if q == 'quest_8':
        return render(request, 'quiz/game/q8.html')