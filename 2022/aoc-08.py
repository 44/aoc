import sys

def get_test():
    trees = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390" ]
    return trees

def rotate(original):
    return list(zip(*original[::-1]))

def parse_input(lines):
    result = []
    y = 0
    for l in lines:
        row = []
        x = 0
        for c in l.strip():
            row.append( (int(c), x, y) )
            x += 1
        result.append(row)
        y += 1
    return result

def get_visible_in_row(row):
    result = set()
    max_height = -1
    for t in row:
        if t[0] > max_height:
            result.add(t)
            max_height = t[0]
    return result

def count_visible(forest):
    all_visible = set()
    for d in range(4):
        for row in forest:
            visible = get_visible_in_row(row)
            all_visible = all_visible.union( visible )
        forest = rotate(forest)
    return all_visible

def scenic_row_scores(row, scores):
    for i in range(len(row)):
        t = row[i]
        score = 0
        for j in range(i + 1, len(row)):
            if row[j][0] >= t[0]:
                score += 1
                break
            score += 1
        scores[ (t[1], t[2], ) ] = scores[ (t[1], t[2],) ] * score

def scenic_score(forest):
    from collections import defaultdict
    scores = defaultdict(lambda: 1)
    for d in range(4):
        for row in forest:
            scenic_row_scores(row, scores)
        forest = rotate(forest)
    return scores


def print_forest(forest, visible):
    i = 0
    for row in forest:
        str_row = ''
        j = 0
        for column in row:
            if not visible is None:
                if (column[0], j, i) in visible:
                    str_row += str(column[0])
                else:
                    str_row += "_"
            else:
                str_row += str(column[0])
            j += 1
        print(str_row)
        i += 1

if __name__ == "__main__":
    #test()
    t = parse_input(["321", "111", "456"])
    #print(t, rotate(t))
    print_forest(t, None)
    v = count_visible(t)
    print('visible', len(v))
    print_forest(t, v)
    print('====')
    t = parse_input(get_test())
    print_forest(t, None)
    v = count_visible(t)
    print('visible', len(v))
    print_forest(t, v)
    scores = scenic_score(t)
    print('max scenic score', max(scores.values()))
    print('====')
    with open('input-08.txt') as file:
        lines = [line.rstrip() for line in file]
        t = parse_input(lines)
        print_forest(t, None)
        v = count_visible(t)
        print('visible', len(v))
        print_forest(t, v)
        scores = scenic_score(t)
        print('max scenic score', max(scores.values()))

