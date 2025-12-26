import sys


if len(sys.argv) == 1:
    print("No scores provided. Usage:", end="")
    print(" python3 ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []
    try:
        i = 1
        while i < len(sys.argv):
            x = int(sys.argv[i])
            if 0 >= x:
                raise Exception("negative value!, let me fix this!")
            elif x >= 99999:
                raise Exception("Holy cow! this is really score!")
            scores.append(x)
            i += 1
    except Exception:
        print("oops, I typed ’banana’ instead of ’1000’")
    else:
        total_players = len(sys.argv) - 1
        total_score = 0
        for score in scores:
            total_score += score
        average_score = total_score / total_players
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score
        print("=== Player Score Analytics ===")
        print("Scores processed: [", end="")
        i = 0
        while i < len(scores):
            print(f"{scores[i]}", end="")
            if i != len(scores) - 1:
                print(", ", end="")
            else:
                print("]")
            i += 1
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
