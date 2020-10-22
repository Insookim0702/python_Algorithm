def solution(votes, k):
    answer = ''
    s = set()
    new_votes = []
    for i in votes:
        s.add(i)
    for i in s:
        new_votes.append((votes.count(i), i))

    new_votes.sort(key= lambda x : (-x[0], x[1]), reverse=True)
    top_rank_vote = 0
    down_rank_vote = 0
    for i in range(k):
        top_rank_vote += new_votes[len(new_votes)-1 - i][0]
    last_model = ''
    while True:
        vote, model = new_votes.pop(0)
        down_rank_vote += vote
        if down_rank_vote >= top_rank_vote:
            return last_model
        last_model = model
    return last_model


print(solution(["AAD", "AAA", "AAC", "AAB"], 4))