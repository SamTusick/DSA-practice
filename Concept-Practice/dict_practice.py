
def main():
    people = []
    people.append({'name': 'Sam', 'age': 20, 'major': 'SWE'})
    people.append({'name': 'Erik', 'age': 19, 'major': 'Prenursing'})

    #print(people)

    #for person in people:
        #if person['name'] == 'Erik':
            #print(person)


    people_dict = {
        'Sam': {'age': 20, 'major': 'SWE'}, 
        'Erik': {'age': 19, 'major': 'Prenursing'}
    }

    if 'Will' in people_dict:
        print("WooHoo")
    else:
        print('Nope')

    print(people_dict)
    print(people_dict['Sam'])
    print(people_dict['Erik']['age'])

if __name__ == "__main__":
    main()