from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = ["bob"]
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]

    searched = {}

    # while the search queue is not empty
    while search_queue:
        # pop the first person off the queue
        person = search_queue.popleft()
        if person in searched:
            continue
        # check if person is a mango seller
        if person_is_seller(person):
            # if they are a seller, print their name, and exit
            print(person + " is a mango seller!")
            return
        else:
            # otherwise, add all of their friends to the search queue
            searched[person] = True
            search_queue += graph[person]

search("you")