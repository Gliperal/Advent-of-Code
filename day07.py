import file_input
lines = file_input.get_input(7)

def find_containers(bag, containers):
    for line in lines:
        if bag in line and not line.startswith(bag):
            bigger_bag = line.split(' bags contain ')[0]
            if bigger_bag not in containers:
                containers.add(bigger_bag)
                find_containers(bigger_bag, containers)

def part1():
    containing_bags = set()
    find_containers('shiny gold', containing_bags)
    print(len(containing_bags))

def count_bags(bags, name):
    bag = bags[name]
    if 'holds' not in bag:
        total = 0
        for group in bag['contents']:
            s = group.split(' ', 1)
            group_count = int(s[0])
            group_name = s[1]
            total += group_count * (1 + count_bags(bags, group_name))
        bag['holds'] = total
    return bag['holds']

def part2():
    bags = dict()
    for line in lines:
        s = line.split(' bags contain ')
        name = s[0]
        bag = {'name': name}
        if 'no other bags' in s[1]:
            bag['contents'] = []
            bag['holds'] = 0
        else:
            bag['contents'] = [
                group.strip(' .\n').rsplit(' ', 1)[0] for
                group in s[1].split(',')
            ]
        bags[name] = bag
    print(count_bags(bags, 'shiny gold'))

#part1()
part2()
