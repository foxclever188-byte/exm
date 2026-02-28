
def dat(count, total, high, low, score):
    new_count = count + 1
    new_total = total + score
    if score > high:
        new_high = score
    else:
        new_high = high
    if score < low:
        new_low = score
    else:
        new_low = low
    return new_count, new_total, new_high, new_low
if __name__ == "__main__":
    count = 0
    total = 0
    high = 0
    low = 100
    print("Type your scores. Type 'done' to stop.")
    while True:
        entry = input("Enter score: ")
        if entry == "done":
            break
        score = int(entry)
        count, total, high, low = dat(count, total, high, low, score)
    if count > 0:
        print("Total Students:", count)
        print("Average Score:", total / count)
        print("Highest:", high)
        print("Lowest:", low)