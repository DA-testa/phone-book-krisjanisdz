# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
         self.name = query[2]

class PhoneBook:
    def __init__(self):
        self.contacts = {}
    
    def add(self, number, name):
        self.contacts[number] = name

    def delete(self, number):
        if number in self.contacts:
            del self.contacts[number]
    
    def find(self, number):
        return self.contacts.get(number, "not found")
    
def read_queries():
    n = int(input())
    if n < 1 or n > 100000:
        print("wrong input")
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    contact_list = PhoneBook()
    result = []
    for query in queries:
        if query.type == "add":
            contact_list.add(query.number, query.name)
        elif query.type == "del":
            contact_list.delete(query.number)
        elif query.type == "find":
            result.append(contact_list.find(query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

#class Query:
  #  def __init__(self, query):
        #self.type = query[0]
        #self.number = int(query[1])
       # if self.type == 'add':
           # self.name = query[2]

#def read_queries():
    #n = int(input())
    #if n < 1 or n > 100000:
      #  print("wrong input")
  #  return [Query(input().split()) for i in range(n)]

#def write_responses(result):
    #print('\n'.join(result))

#def process_queries(queries):
   # result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
   # contacts = []
    #for cur_query in queries:
     #   if cur_query.type == 'add':
      #      # if we already have contact with such number,
            # we should rewrite contact's name
       #     for contact in contacts:
        #        if contact.number == cur_query.number:
         #           contact.name = cur_query.name
          #          break
           # else: # otherwise, just add it
            #    contacts.append(cur_query)
        #elif cur_query.type == 'del':
         #   for j in range(len(contacts)):
          #      if contacts[j].number == cur_query.number:
           #         contacts.pop(j)
            #        break
        #else:
         #   response = 'not found'
          #  for contact in contacts:
           #     if contact.number == cur_query.number:
            #        response = contact.name
             #       break
            #result.append(response)
    #return result

#if __name__ == '__main__':
 #   write_responses(process_queries(read_queries()))

